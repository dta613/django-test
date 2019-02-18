"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.urls import path
from django.contrib import admin
import myapp
from myapp.views import login as login
from myapp.views import logout as logout
from myapp.views import signup as signup
from myapp.views import index as index
from rest_framework import routers, serializers, viewsets
from myapp.models import Patient

# Serializers define the API representation.
class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('Patient_firstname', 'Patient_lastname')

# ViewSets define the view behavior.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'patient', PatientViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
#For other experience outside of API
    url(r'^admin', admin.site.urls),
    url(r'^logout/', logout, name='logout'),
    url(r'^signup/', signup, name='signup'),
    url(r'^login/', login, name='login'),
    url(r'^$', index, name='index'),
]
