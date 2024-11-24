from django.db import models

class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.nome
