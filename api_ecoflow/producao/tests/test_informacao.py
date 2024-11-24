from django.test import TestCase
from producao.models.informacao import InformacaoProducao
from producao.models.produtor import Produtor
from producao.models.lote import Lote

class InformacaoProducaoTestCase(TestCase):
    def setUp(self):
        self.produtor = Produtor.objects.create(
            nome="Maria Oliveira",
            email="maria@exemplo.com"
        )
        self.lote = Lote.objects.create(
            identificador="Lote002"
        )
        self.informacao = InformacaoProducao.objects.create(
            lote=self.lote,
            produtor=self.produtor,
            descricao="Informação de teste",
            quantidade_agua=120.5,
            emissao_carbono=30.8
        )

    def test_criar_informacao(self):
        self.assertEqual(self.informacao.descricao, "Informação de teste")
        self.assertEqual(self.informacao.quantidade_agua, 120.5)
