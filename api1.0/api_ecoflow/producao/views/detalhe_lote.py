from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Lote

def detalhe_lote(request, identificador):
    lote = get_object_or_404(Lote, identificador=identificador)
    return JsonResponse({
        'id': lote.id,
        'produtor': lote.produtor.nome,
        'informacoes': list(lote.informacoes.values())
    })
