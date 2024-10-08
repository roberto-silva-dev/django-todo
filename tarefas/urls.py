from django.urls import path
from .views import *

urlpatterns = [
    path('', tarefa_listar, name='tarefa_listar'),
    path('criar', tarefa_criar, name='tarefa_criar'),
    path('editar/<int:tarefa_id>', tarefa_editar, name='tarefa_editar'),
    path('deletar/<int:tarefa_id>', tarefa_deletar, name='tarefa_deletar'),
]
