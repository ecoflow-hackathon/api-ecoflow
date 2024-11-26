from rest_framework import viewsets
from .models import Produtor
from .serializers import ProdutorSerializer

class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer