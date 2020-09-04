from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'writings/', include('writings.urls')),
    url(r'^about/$', views.about),
    url('', views.homepage),
]
