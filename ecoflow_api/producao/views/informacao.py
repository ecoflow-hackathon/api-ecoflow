from rest_framework import viewsets
from producao.models.informacao import InformacaoProducao
from producao.serializers.informacao import InformacaoProducaoSerializer

class InformacaoProducaoViewSet(viewsets.ModelViewSet):
    queryset = InformacaoProducao.objects.all()
    serializer_class = InformacaoProducaoSerializer
