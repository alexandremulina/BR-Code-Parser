# BRQR
Ao unificar códigos QR, o Banco Central procurou facilitar a iniciação de uma transação de pagamento.O objetivo desta biblioteca é extrair todas as informações contidas no "BR CODE".Meu Objetivo aqui é extrair todas as informaçoes existentes neste padrão de QRCode, mostrando meus pontos de abordagens e motivos por tras deles.





# Vamos do inicio...

Primeiramente voce preciara extrair o "data" do seu QRCode, e para isso utilizei duas bibliotecas, que são:

⦁	Pillow 

⦁	pyzbar


Vou deixar aqui um exemplo de como estou extraindo meu **data** do QRCode. Lembrando que existem outras formas de o fazer.
```python
from pyzbar.pyzbar import decode
from PIL import Image

import brqr
from brqr import QR

d = decode(Image.open('C:/...qrcode.png'))
data = d[0].data.decode('ascii')
```


# Caracteristicas do BR CODE

![](https://github.com/alexandremulina/brqr/blob/master/TabelaPradr%C3%A3o.jpg?raw=true)

Acima temos a estrutura comum de um BR CODE


Dentro deste padrão existem dois tipos:

⦁	**QR Code Estático**



![](https://github.com/alexandremulina/brqr/blob/master/QREstatico.jpg?raw=true)
![](https://github.com/alexandremulina/brqr/blob/master/QREstatico2.jpg?raw=true)

⦁ **QR Code Dinâmico**


![](https://github.com/alexandremulina/brqr/blob/master/QRDinamico1.jpg?raw=true)
![](https://github.com/alexandremulina/brqr/blob/master/QRDinamico2.jpg?raw=true)
![](https://github.com/alexandremulina/brqr/blob/master/QRDinamico3.jpg?raw=true)
![](https://github.com/alexandremulina/brqr/blob/master/QRDinamico4.jpg?raw=true)
![](https://github.com/alexandremulina/brqr/blob/master/QRDinamico5.jpg?raw=true)




# Objetivo

Meu principal objetivo aqui foi recolher todas as informações dentro do BR CODE, incialmente meu pensamento era fazer uma diferença entre eles e é algo que pode ser feito furutamente.Porém de inicio, conseguir extrair informaçoes tanto de um QR Dinâmico quanto um QR Estático me pareceu mais lógico e efetivo.

# Como Usar


