from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('passwd-generator', views.passwd_gen, name='Generator')
]