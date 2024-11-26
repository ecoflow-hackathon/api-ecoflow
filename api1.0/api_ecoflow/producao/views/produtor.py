from rest_framework import viewsets
from producao.models.produtor import Produtor
from producao.serializers.produtor import ProdutorSerializer

class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
