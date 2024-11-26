from rest_framework import viewsets
from .models import Lote
from .serializers import LoteSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

def detalhe_lote(request, identificador):
    lote = get_object_or_404(Lote, identificador=identificador)
    return JsonResponse({
        'id': lote.id,
        'produtor': lote.produtor.nome,
        'informacoes': list(lote.informacoes.values())
    })