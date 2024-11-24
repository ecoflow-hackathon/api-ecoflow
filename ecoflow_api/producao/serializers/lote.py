from rest_framework import serializers
from producao.models.lote import Lote
from producao.models.informacao import InformacaoProducao
from producao.serializers.informacao import InformacaoProducaoSerializer

class LoteSerializer(serializers.ModelSerializer):
    informacoes = InformacaoProducaoSerializer(many=True, read_only=True)

    class Meta:
        model = Lote
        fields = '__all__'
