import qrcode
from io import BytesIO
from django.core.files import File

def gerar_qrcode(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return File(buffer, name='qrcode.png')
