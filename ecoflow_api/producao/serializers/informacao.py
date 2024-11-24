from rest_framework import serializers
from producao.models.informacao import InformacaoProducao

class InformacaoProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacaoProducao
        fields = '__all__'
