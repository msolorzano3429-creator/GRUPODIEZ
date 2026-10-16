from django.urls import path

from Core import views


urlpatterns = [
     path('', views.log_in, name='members'),
     path('corto/', views.corto, name='corto'),
     path('members/', views.home, name='home'),
     path('members/crearusuario/', views.registro, name='CrearUsuario'),
     path('bootstrap_builder/', views.bootstrap_builder, name='bootstrap_builder'),
     path('contact/', views.contact, name='contact'),
     path('admin/', views.admin, name='admin'),
     path('business/', views.business, name='business'),
     path('education/', views.education, name='education'),
     path('portfolio/', views.portfolio, name='Portafolio'),
     path('portfolio_builder/', views.portfolio_builder, name='portfolio_builder'),
     path('license/', views.license, name='license'),
     path('premium/', views.premium, name='premium'),

]