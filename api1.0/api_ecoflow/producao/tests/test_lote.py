from django.test import TestCase
from producao.models.lote import Lote
from producao.models.produtor import Produtor

class LoteTestCase(TestCase):
    def setUp(self):
        self.produtor = Produtor.objects.create(
            nome="João da Silva",
            email="joao@exemplo.com"
        )
        self.lote = Lote.objects.create(
            identificador="Lote001"
        )
        self.lote.produtores.add(self.produtor)

    def test_criar_lote(self):
        self.assertEqual(self.lote.identificador, "Lote001")
        self.assertIn(self.produtor, self.lote.produtores.all())
