from django.urls import path
from core.erp.views.alumnas.views import *

app_name = 'erp'

urlpatterns = [
    path('alumnas/listado/', AlumnasListView.as_view(), name='alumnas_listado'),
    path('alumnas/nueva/', AlumnasCreateView.as_view(), name='alumnas_crear'),
    path('alumnas/editar/<int:pk>/', AlumnasUpdateView.as_view(), name='alumnas_editar'),
    path('alumnas/borrar_ajax/', alumnas_borrar_ajax, name='alumnas_borrar_ajax'),

    path('alumnas/cumpleaños/', birthdays_get_list_ajax, name='birthdays_get_list_ajax'),
]
