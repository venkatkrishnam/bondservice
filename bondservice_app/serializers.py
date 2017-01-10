
from rest_framework import serializers

from .models import Bond

class BondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = ('cusip', 'issuer', 'currency', 'issueDate', 'maturityDate', 'parValue', 'coupon', 'payFrequency', 'settleDelay', 'description')