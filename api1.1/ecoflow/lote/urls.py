from django.urls import path
from .views import LoteViewSet, detalhe_lote

urlpatterns = [
    path('all/', LoteViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('lote/<str:pk>/', LoteViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('lote/<str:identificador>/', detalhe_lote, name='detalhe_lote')
]