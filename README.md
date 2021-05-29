# BRCODE
O Banco Central anunciou a criação de um padrão único para QR Codes, a serem usados nos meios de pagamento de empresas integrantes do Sistema de Pagamentos Brasileiro (SPB).O objetivo desta biblioteca é extrair todas as informações contidas no "BR CODE", mostrando minhas abordagens.



![](https://i.pinimg.com/originals/e4/af/9f/e4af9f0025a8ce68bee2cf5a1360a501.gif)

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





⦁ **QR Code Dinâmico**




Para saber mais de suas caracteristas e para melhor leitura, vou disponibilizar o arquivo em pdf que foi  minha bases nesse projeto.

[Manual do BR Code.pdf](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix-versao1.pdf)



# Objetivo

Meu principal objetivo aqui foi recolher todas as informações dentro do BR CODE,previamente o objetivo era fazer um codigo no qual fosse identificar uma diferença entre o dinâmico e o estático,mas deixo isso para o futuro.De início, conseguir extrair informaçoes tanto de um QR Dinâmico quanto um QR Estático me pareceu mais lógico e efetivo.

# Como Usar

```Python
from pyzbar.pyzbar import decode
from PIL import Image

import brqr
from brqr import QR



d = decode(Image.open('C:/.../qrcode.png'))
data = d[0].data.decode('ascii')


print(type(QR(data).PFI))
print(QR(data).PFI)
print(QR(data).PIM)
print(QR(data).MAI)
print(QR(data).MAI_GUI)
print(QR(data).MAI_CHAVEPIX)
print(QR(data).INF_ADD)
print(QR(data).MAI_URL)
print(QR(data).MAI_INST)
print(QR(data).MAI_TIPO)
print(QR(data).MAI_AG)
print(QR(data).MAI_CONTA)
print(QR(data).MAI_OUTRO_GUI)
print(QR(data).MAI_OUTRO_IDCONTA)
print(QR(data).MCC)
print(QR(data).TC)
print(QR(data).TA)
print(QR(data).CC)
print(QR(data).MN)
print(QR(data).MC)
print(QR(data).PC)
print(QR(data).ADF_REF)
print(QR(data).ADF_VER)
print(QR(data).Ver)
print(QR(data).UT_GUI)
print(QR(data).UT_URL)
print(QR(data).UT2_GUI)
print(QR(data).UT2_OUT)
print(QR(data).CRC)
```
```
01
Não Informado
12345678901234
BR.GOV.BCB.PIX
66756C616E6F32303139406578616D706C652E636F6D
Não Informado
Não Informado
Não Informado
Não Informado
BR.COM.OUTRO
0123456789
0000
986
123.45
BR
NOMEDORECEBEDOR
BRASILIA
70074900
RP12345678-2019
BR.GOV.BCB.BRCODE
1.0.0
BR.GOV.BCB.PIX
PADRAO.URL.PIX/0123ABCD
BR.COM.OUTRO
0123.ABCD.3456.WXYZ
EB76
[Finished in 1.0s]
```




> pip install brqr==1.21



