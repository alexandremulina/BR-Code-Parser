from pyzbar.pyzbar import decode
from PIL import Image
import pandas as pd
import brqr
from brqr import QR

d = decode(Image.open('C:/Users/alexa/OneDrive/Documentos/qrcode.png'))
df = pd.DataFrame(d)
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('max_colwidth', None)
data = d[0].data.decode('ascii')



data = d[0].data.decode('ascii')

def Cut_Str(data):
	New_Data = data[2:]
	return  New_Data


def Shorten(data):
	Data1 = Cut_Str(data)
	Size = Data1[:2]
	Size_int = int(Size)
	Data2 = Cut_Str(Data1)
	Value = Data2[:Size_int]
	Data3 = Data2[Size_int:]
	return Data3,Value

Manual = {'00':{'00':{'PFI':'Value'}},
'01':{'01':{'PIM':'Value'}},
'04':{'MAI_Cartoes':'Value'},
'26':{'00':{'MAI_GUI':'Value'},'01':{'MAI_CHAVEPIX':'Value'},'21':{'MAI_INST':'Value'},'22':{'MAI_TPCONTA':'Value'},'23':{'MAI_AG':'Value'},'24':{'MAI_CONTA':'Value'}},
'27':{'MAI2':'Value'},
'52':{'MCC':'Value'},
'53':{'TC':'Value'},
'54':{'TA':'Value'},
'58':{'CC':'Value'},
'59':{'MN':'Value'},
'60':{'MC':'Value'},
'61':{'PC':'Value'},
'62':{'05':{'ADF_REF':'Value'},'50':{'ADF_VER':'Value'}},
'80':{'0':{'UT_GUI':'Value'},'1':{'UT_URL':'Value'}},
'81':{'0':{'UT_GUI':'Value'},'1':{'UT_URL':'Value'}},
'63':{'CRC':'Value'}}

print(data)


for key in Manual:

	if key ==data[:2]:
		Data3, Manual[key][key] = Shorten(data)
		data = Data3


	else:
		print(Manual[key],'Não informado')



	print(Manual[key])
