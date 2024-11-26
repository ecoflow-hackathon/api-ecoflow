from django.db import models
from django.core.exceptions import ValidationError

class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    is_admin = models.BooleanField(default=False)
    cnpj = models.CharField(max_length=14, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome
    
    def clean(self):
        if self.is_admin and not self.cnpj:
            raise ValidationError('CNPJ não pode ser nulo se is_admin for True.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
