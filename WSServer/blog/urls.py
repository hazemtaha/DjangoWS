

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^index$', views.index,name="index"),
    url(r'^login$', views.login,name="login"),
    url(r'^registration$', views.registration,name="registration"),
]
STATIC_URL = '/static/'