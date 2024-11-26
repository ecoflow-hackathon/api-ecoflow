from django.urls import path
from .views import ProdutorViewSet

urlpatterns = [
    path('produtor/', ProdutorViewSet.as_view({'get': 'list', 'post': 'create'})),
]