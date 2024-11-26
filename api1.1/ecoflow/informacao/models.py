from django.db import models
from lote.models import Lote
from produtor.models import Produtor

class InformacaoProducao(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='informacoes')
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, related_name='informacoes_enviadas')
    descricao = models.TextField()
    quantidade_agua = models.FloatField(blank=True, null=True)
    emissao_carbono = models.FloatField(blank=True, null=True)
    quantidade_energia = models.FloatField(blank=True, null=True)
    quantidade_residuos = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Informação de {self.produtor.nome} no Lote {self.lote.identificador}"