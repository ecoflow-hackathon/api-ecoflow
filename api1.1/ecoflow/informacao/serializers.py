from rest_framework import serializers
from .models import InformacaoProducao

class InformacaoProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacaoProducao
        fields = '__all__'
