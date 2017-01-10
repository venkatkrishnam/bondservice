import logging

from django.shortcuts import render
from django.http import Http404

from rest_framework import *
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import Bond
from .serializers import BondSerializer

class BondList(APIView):
	permission_classes = [permissions.AllowAny,]	
	serializer = BondSerializer()
	logger = logging.getLogger(__name__)

	def get_serializer(self):
		return self.serializer

	def get(self, request, format=None):
		bonds = Bond.objects.all()
		serializer = BondSerializer(bonds, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = BondSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			json = JSONRenderer().render(serializer.data)
			print(json)
			return Response(json, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BondDetail(APIView):
	permission_classes = [permissions.AllowAny,]
	serializer = BondSerializer()

	def get_serializer(self):
		return self.serializer

	def get_object(self, pk):
		try:
			return Bond.objects.get(pk=pk)
		except Bond.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		bond = self.get_object(pk)
		bond = BondSerializer(bond)
		return Response(bond.data)

	def put(self, request, pk, format=None):
		bond = self.get_object(pk)
		serializer = BondSerializer(bond, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		bond = self.get_object(pk)
		bond.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)