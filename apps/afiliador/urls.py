from django.urls import path, include

from apps.afiliador.views import index, afiliador_view, afiliador_list, afiliador_edit, afiliador_delete, AfiliadorList

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', afiliador_view, name='afiliador_crear'), #basado en funciones
    # path('listar', afiliador_list, name='afiliador_listar'), #basado en funciones
    path('listar', AfiliadorList.as_view(), name='afiliador_listar'), #basado en clases
    path('editar/<id_afiliador>/', afiliador_edit, name='afiliador_editar'), #basado en funciones
    path('eliminar/<id_afiliador>/', afiliador_delete, name='afiliador_eliminar'), #basado en funciones
]
