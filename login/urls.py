from django.urls import path
from . import views

urlpatterns = [ 
    path('tela_login/', views.tela_login, name='tela_login'),
    path('tela_login/tela_cadastro.html', views.tela_cadastro, name='cadastramento' )]
   