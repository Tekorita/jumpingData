from django.urls import path, include

from apps.sede.views import index, sede_view, sede_list, sede_edit, sede_delete, SedeList

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', sede_view, name='sede_crear'), #basado en funciones
    # path('listar', sede_list, name='sede_listar'), #basado en funciones
    path('listar', SedeList.as_view(), name='sede_listar'), #basado en clases
    path('editar/<id_sede>/', sede_edit, name='sede_editar'), #basado en funciones
    path('eliminar/<id_sede>/', sede_delete, name='sede_eliminar'), #basado en funciones
]
