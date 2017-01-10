from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from bondservice_app import views

schema_view = get_schema_view(title='Bond API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

admin.autodiscover()

urlpatterns = [

	url(r'^$', schema_view, name='docs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bonds/', views.BondList.as_view()),
    url(r'^bond/(?P<pk>[0-9]+)/$', views.BondDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]