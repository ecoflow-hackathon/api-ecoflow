from django.test import TestCase
from producao.models.produtor import Produtor

class ProdutorTestCase(TestCase):
    def setUp(self):
        self.produtor = Produtor.objects.create(
            nome="João da Silva",
            email="joao@exemplo.com",
            telefone="123456789"
        )

    def test_criar_produtor(self):
        self.assertEqual(self.produtor.nome, "João da Silva")
        self.assertEqual(self.produtor.email, "joao@exemplo.com")
