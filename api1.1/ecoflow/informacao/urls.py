from django.urls import path
from .views import InformacaoProducaoViewSet

urlpatterns = [
    path('informacao-producao/', InformacaoProducaoViewSet.as_view({'get': 'list', 'post': 'create'})),
]
