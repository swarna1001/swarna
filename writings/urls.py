from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'writings'

urlpatterns = [
    url(r'^$', views.writings_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.writings_detail, name="detail"),
]
