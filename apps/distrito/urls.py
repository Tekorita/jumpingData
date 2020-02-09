from django.urls import path, include

from apps.distrito.views import index, distrito_view, distrito_list, distrito_edit, distrito_delete, DistritoList

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', distrito_view, name='distrito_crear'), #basado en funciones
    # path('listar', distrito_list, name='distrito_listar'), #basado en funciones
    path('listar', DistritoList.as_view(), name='distrito_listar'), #basado en clases
    path('editar/<id_distrito>/', distrito_edit, name='distrito_editar'), #basado en funciones
    path('eliminar/<id_distrito>/', distrito_delete, name='distrito_eliminar'), #basado en funciones
]
