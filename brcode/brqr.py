#Autor : Osmar Alexandre da Silva Mulina Pereira
#Data: 19/09/2020

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


class QR():
	def __init__(self,data):
		self.data =data
		if data[:2] == '00':
			Data3, self.PFI = Shorten(data)
		else:
			self.PFI = 'Não Informado'

		if Data3[:2] =='01':
			Data3,self.PIM = Shorten(Data3)
		else:
			self.PIM = 'Não Informado'
		
		if Data3[:2] =='04':
			Data3, self.MAI = Shorten(Data3)
		else:
			self.MAI = 'Não Informado'
		MAIPIX_id = Data3[:2]
		MAIXPIX_id_int =  int(MAIPIX_id)
		if (MAIXPIX_id_int >25 & MAIXPIX_id_int< 51):
			Data7 = Cut_Str(Data3)
			MP_TAM = Data7[:2]
			MP_TAM_int = int(MP_TAM)
			Data8 = Cut_Str(Data7)
			Sub_Data = Data8[:MP_TAM_int]
			MPGUI_id = Sub_Data[:2]
			if MPGUI_id =='00':
				Data3,self.MAI_GUI = Shorten(Sub_Data)
				MP_CHAVE_INST_id = Data3[:2]
				Sub_data = Data3
			if MP_CHAVE_INST_id == '01':
				Sub_data,self.MAI_CHAVEPIX = Shorten(Data3)
				
			
			else:
				self.MAI_CHAVEPIX = 'Não Informado'
			if Sub_data == '03':
				Sub_data,self.INF_ADD = Shorten(Data3)
				
			
			else:
				self.INF_ADD = 'Não Informado'

			if MP_CHAVE_INST_id == '21':
				Sub_Data,self.MAI_INST = Shorten(Data3)
				Sub_Data,self.MAI_TIPO = Shorten(Sub_Data)
				Sub_Data,self.MAI_AG = Shorten(Sub_Data)
				Sub_Data,self.MAI_CONTA = Shorten(Data3)
				Data3 = Data8[MP_TAM_int:]

			else:
				self.MAI_INST = 'Não Informado'
				self.MAI_TIPO = 'Não Informado'
				self.MAI_AG= 'Não Informado'
				self.MAI_CONTA = 'Não Informado'
				
			if MP_CHAVE_INST_id == '25':
				Sub_Data,self.MAI_URL= Shorten(Data3)
				Data3 = Data8[MP_TAM_int:]
			else:
				self.MAI_URL='Não Informado'
				Data3 = Data8[MP_TAM_int:]


		if (Data3[:2] =='27'):
			Data10 = Cut_Str(Data3)
			MAI_OUT_TAM = Data10[:2]
			MAI_OUT_TAM_int = int(MAI_OUT_TAM)
			Data11=Cut_Str(Data10)
			Sub_data = Data11[:MAI_OUT_TAM_int]
			Data3,self.MAI_OUTRO_GUI = Shorten(Sub_data)
			Data3,self.MAI_OUTRO_IDCONTA = Shorten(Data3)
			Data3 = Data11[MAI_OUT_TAM_int:]
		else:
			self.MAI_OUTRO_IDCONTA = 'Não Informado'
			self.MAI_OUTRO_GUI = 'Não Informado'
		if Data3[:2] == '52':
			Data3, self.MCC = Shorten(Data3)
		else:
			self.MCC = 'Não Informado'
		
		if Data3[:2] =='53':
			Data3, self.TC = Shorten(Data3)
		else:
			self.TC = 'Não Informado'
		
		if Data3[:2] =='54':
			Data3, self.TA = Shorten(Data3)
		else:
			self.TA= 'Não Informado'
		
		if Data3[:2] == '58':
			Data3, self.CC = Shorten(Data3)
		else:
			self.CC = 'Não Informado'
		
		if Data3[:2] =='59':
			Data3, self.MN = Shorten(Data3)
		else:
			self.MN = 'Não Informado'
	
		if Data3[:2] =='60':
			Data3, self.MC = Shorten(Data3)
		else:
			self.MC = 'Não Informado'
	
		if Data3[:2] == '61':
			Data3, self.PC = Shorten(Data3)
		else:
			self.PC='Não Informado'
		
		if Data3[:2] =='62':
			Data10 = Cut_Str(Data3)
			ADF_TAM = Data10[:2]
			ADF_TAM_int = int(ADF_TAM)
			Data11 = Cut_Str(Data10)
			if Data11[:2]=='05':
				Data3, self.ADF_REF = Shorten(Data11)
			else:
				self.ADF_VER = 'Não informado'

			if Data3[:2] =='50':
				Data10 = Cut_Str(Data3)
				ADF_VER_TAM = Data10[:2]
				ADF_VER_TAM_int = int(ADF_VER_TAM)
				Data11 = Cut_Str(Data10)
				ADF_VER_id = Data11[:2]
				Data12 = Cut_Str(Data11)
				ADF_VER_TAM =Data12[:2]
				ADF_VER_TAM_int =int (ADF_VER_TAM)
				Data13 = Cut_Str(Data12)
				self.ADF_VER= Data13[:ADF_VER_TAM_int]
				Data14 = Data13[ADF_VER_TAM_int:]
				Data3, self.Ver= Shorten(Data14)
			else:
				self.Ver ='Não informado'
				self.ADF_VER = 'Não Informado'
				
				
			
		else:
			self.ADF_REF = 'AD Field Não informado'
			self.ADF_VER = 'Não informado'
			self.Ver = 'Não informado'
		if Data3[:2]=='80':
			Data10 = Cut_Str(Data3)
			UT_TAM = Data10[:2]
			Data11 =Cut_Str(Data10)
			Data3, self.UT_GUI = Shorten(Data11)
			Data3, self.UT_URL = Shorten(Data3)
			
		else:
			self.UT_GUI = 'Não informado'
			self.UT_URL = 'Não Informado'
		if Data3[:2] =='81':
			Data3 = Cut_Str(Data3)
			UTemp_TAM = Data3[:2]
			Data11 =Cut_Str(Data3)
			Data3, self.UT2_GUI = Shorten(Data11)
			Data3, self.UT2_OUT = Shorten(Data3)
		else:
			self.UT2_GUI = 'Não Informado'
			self.UT2_OUT = 'Não Informado'
		if Data3[:2] =='63':
			Data10 = Cut_Str(Data3)
			CRC_TAM = Data10[:2]
			CRC_TAM_int = int(CRC_TAM)
			Data11 = Cut_Str(Data10)
			self.CRC = Data11[:CRC_TAM_int]
		else:
			self.CRC ='Não informado'
