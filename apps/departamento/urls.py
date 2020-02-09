from django.urls import path, include

from apps.departamento.views import index, departamento_view, departamento_list, departamento_edit, departamento_delete, DepartamentoList

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', departamento_view, name='departamento_crear'), #basado en funciones
    # path('listar', departamento_list, name='departamento_listar'), #basado en funciones
    path('listar', DepartamentoList.as_view(), name='departamento_listar'), #basado en clases
    path('editar/<id_departamento>/', departamento_edit, name='departamento_editar'), #basado en funciones
    path('eliminar/<id_departamento>/', departamento_delete, name='departamento_eliminar'), #basado en funciones
]
