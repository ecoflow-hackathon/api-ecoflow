from django.db import models
from .produtor import Produtor

class Lote(models.Model):
    identificador = models.CharField(max_length=50, unique=True)
    produtores = models.ManyToManyField(Produtor, related_name='lotes')
    criado_em = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return self.identificador

    def save(self, *args, **kwargs):
        qr_data = f"http://seu-dominio.com/lote/{self.identificador}"
        qr_image = qrcode.make(qr_data)
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        self.qr_code.save(f"{self.identificador}_qrcode.png", ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)
