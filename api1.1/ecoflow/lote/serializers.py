from rest_framework import serializers
from .models import Lote
from informacao.serializers import InformacaoProducaoSerializer

class LoteSerializer(serializers.ModelSerializer):
    informacoes = InformacaoProducaoSerializer(many=True, read_only=True)

    class Meta:
        model = Lote
        fields = '__all__'