from django.urls import path, include

from apps.campaña.views import index, campaña_view, campaña_list, campaña_edit, campaña_delete, CampañaList

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', campaña_view, name='campaña_crear'), #basado en funciones
    # path('listar', campaña_list, name='campaña_listar'), #basado en funciones
    path('listar', CampañaList.as_view(), name='campaña_listar'), #basado en clases
    path('editar/<id_campaña>/', campaña_edit, name='campaña_editar'), #basado en funciones
    path('eliminar/<id_campaña>/', campaña_delete, name='campaña_eliminar'), #basado en funciones
]
