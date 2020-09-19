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



Suas caracteristas e para melhor leitura, vou disponibilizar os dois arquivos em pdf no qual foram minhas bases nesse projeto.

# Objetivo

Meu principal objetivo aqui foi recolher todas as informações dentro do BR CODE, incialmente meu pensamento era fazer uma diferença entre eles e é algo que pode ser feito furutamente.Porém de inicio, conseguir extrair informaçoes tanto de um QR Dinâmico quanto um QR Estático me pareceu mais lógico e efetivo.

# Como Usar

```Python
from pyzbar.pyzbar import decode
from PIL import Image

import brqr
from brqr import QR



d = decode(Image.open('C:/Users/alexa/Documents/qrcode/qrcode.png'))
data = d[0].data.decode('ascii')


print(QR(data).PFI_value)
print(QR(data).PIM_value)
print(QR(data).MAI_value)
print(QR(data).MAI_GUI_value)
print(QR(data).MAI_CHAVEPIX_value)
print(QR(data).MAI_INST_value)
print(QR(data).MAI_TIPO_value)
print(QR(data).MAI_AG_value)
print(QR(data).MAI_CONTA_value)
print(QR(data).MAI_OUTRO_GUI_value)
print(QR(data).MAI_OUTRO_IDCONTA_value)
print(QR(data).MCC_value)
print(QR(data).TC_value)
print(QR(data).TA_value)
print(QR(data).CC_value)
print(QR(data).MN_value)
print(QR(data).MC_value)
print(QR(data).PC_value)
print(QR(data).ADF_REF_value)
print(QR(data).ADF_VER_value)
print(QR(data).Ver_value)
print(QR(data).UT_GUI_value)
print(QR(data).UT_URL_value)
print(QR(data).UT2_GUI_value)
print(QR(data).UT2_OUT_value)
print(QR(data).CRC_value)
```

Sei que não fui muito criativo com as variaveis,porém, tudo é sempre mutavel.
PS:** Valor retornado é uma string** , por agora não vi o motivo de converter os valores numéricos recebidos.

# Onde podemos melhorar?

Esse é uma parte especial, se você teve curiosidade em ler a documentação base para esse projeto, verá que apenas foi disponibilizado as característas de QRCode dinâmico e estático do **recebedor**, e alguns informaçoes não ficaram tão claras diante de que mudanças ainda podem ser implementadas, e caso tenha alguma documentação a agregar, isso será muito util.

A maior dificuldade está na possibilidade de mutação do QRCode dinâmico, dentro da documentação foram fornecidos dois tipos distintos cada um com suas características.

A linha 26 (Marchant Account Information) , para mim ela é a parte mais importante do QRCode, e com isso eu usei um modo diferente de armazenamento 
