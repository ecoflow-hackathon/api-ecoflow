from rest_framework import viewsets
from .models import InformacaoProducao
from .serializers import InformacaoProducaoSerializer

class InformacaoProducaoViewSet(viewsets.ModelViewSet):
    queryset = InformacaoProducao.objects.all()
    serializer_class = InformacaoProducaoSerializer