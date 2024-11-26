from rest_framework import viewsets
from producao.models.lote import Lote
from producao.serializers.lote import LoteSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
