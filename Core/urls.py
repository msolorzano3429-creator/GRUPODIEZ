from django.urls import path

from Core import views


urlpatterns = [
     path('', views.home, name='home'),
     path('corto', views.corto, name='corto'),
 ]