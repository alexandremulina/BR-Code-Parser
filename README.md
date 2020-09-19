# BRQR
Ao unificar códigos QR, o Banco Central procurou facilitar a iniciação de uma transação de pagamento.O objetivo desta biblioteca é extrair todas as informações contidas no "BRCODE".





# Vamos do inicio...


Primeiramente voce preciara extrair o "data" do seu QRCode, e para isso utilizei duas bibliotecas, que são:

⦁	Pillow 

⦁	pyzbar


Vou deixar aqui um exemplo de como estou extraindo meu Data do QRCode. Lmebrando que existem outras formas de o fazer.
```python
from pyzbar.pyzbar import decode
from PIL import Image

import brqr
from brqr import QR

d = decode(Image.open('C:/Users/alexa/Documents/qrcode/qrcode3.png'))
data = d[0].data.decode('ascii')
```






