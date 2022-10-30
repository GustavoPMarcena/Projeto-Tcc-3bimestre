from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Adicionartcc/', views.adicionar, name='adicionartcc'),
    path('visualizartcc/', views.visualizar, name='visualizar'),
    path('editartcc/<int:id>', views.editar, name='editartcc'),
    path('deletartcc/<int:id>', views.deletar, name='deletartcc'),
] 