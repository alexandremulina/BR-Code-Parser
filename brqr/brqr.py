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
			Data3, self.PFI_value = Shorten(data)
		else:
			self.PFI_value = 'Não Informado'

		if Data3[:2] =='01':
			Data3,self.PIM_value = Shorten(Data3)
		else:
			self.PIM_value = 'Não Informado'
		
		if Data3[:2] =='04':
			Data3, self.MAI_value = Shorten(Data3)
		else:
			self.MAI_value = 'Não Informado'
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
				Data3,self.MAI_GUI_value = Shorten(Sub_Data)
				MP_CHAVE_INST_id = Data3[:2]
				Sub_data = Data3
			if MP_CHAVE_INST_id == '01':
				Sub_data,self.MAI_CHAVEPIX_value = Shorten(Data3)
				
			
			else:
				self.MAI_CHAVEPIX_value = 'Não Informado'
			if Sub_data == '03':
				Sub_data,self.INF_ADD_value = Shorten(Data3)
				
			
			else:
				self.INF_ADD_value = 'Não Informado'

			if MP_CHAVE_INST_id == '21':
				Sub_Data,self.MAI_INST_value = Shorten(Data3)
				Sub_Data,self.MAI_TIPO_value = Shorten(Sub_Data)
				Sub_Data,self.MAI_AG_value = Shorten(Sub_Data)
				Sub_Data,self.MAI_CONTA_value = Shorten(Data3)
				Data3 = Data8[MP_TAM_int:]

			else:
				self.MAI_INST_value = 'Não Informado'
				self.MAI_TIPO_value = 'Não Informado'
				self.MAI_AG_value = 'Não Informado'
				self.MAI_CONTA_value = 'Não Informado'
				Data3 = Data8[MP_TAM_int:]

		if (Data3[:2] =='27'):
			Data10 = Cut_Str(Data3)
			MAI_OUT_TAM = Data10[:2]
			MAI_OUT_TAM_int = int(MAI_OUT_TAM)
			Data11=Cut_Str(Data10)
			Sub_data = Data11[:MAI_OUT_TAM_int]
			Data3,self.MAI_OUTRO_GUI_value = Shorten(Sub_data)
			Data3,self.MAI_OUTRO_IDCONTA_value = Shorten(Data3)
			Data3 = Data11[MAI_OUT_TAM_int:]
		else:
			self.MAI_OUTRO_IDCONTA_value = 'Não Informado'
			self.MAI_OUTRO_GUI_value = 'Não Informado'
		if Data3[:2] == '52':
			Data3, self.MCC_value = Shorten(Data3)
		else:
			self.MCC_value = 'Não Informado'
		
		if Data3[:2] =='53':
			Data3, self.TC_value = Shorten(Data3)
		else:
			self.TC_value = 'Não Informado'
		
		if Data3[:2] =='54':
			Data3, self.TA_value = Shorten(Data3)
		else:
			self.TA_value= 'Não Informado'
		
		if Data3[:2] == '58':
			Data3, self.CC_value = Shorten(Data3)
		else:
			self.CC_value = 'Não Informado'
		
		if Data3[:2] =='59':
			Data3, self.MN_value = Shorten(Data3)
		else:
			self.MN_value = 'Não Informado'
	
		if Data3[:2] =='60':
			Data3, self.MC_value = Shorten(Data3)
		else:
			self.MC_value = 'Não Informado'
	
		if Data3[:2] == '61':
			Data3, self.PC_value = Shorten(Data3)
		else:
			self.PC_value='Não Informado'
		
		if Data3[:2] =='62':
			Data10 = Cut_Str(Data3)
			ADF_TAM = Data10[:2]
			ADF_TAM_int = int(ADF_TAM)
			Data11 = Cut_Str(Data10)
			if Data11[:2]=='05':
				Data3, self.ADF_REF_value = Shorten(Data11)
			else:
				self.ADF_VER_value = 'Não informado'

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
				self.ADF_VER_value= Data13[:ADF_VER_TAM_int]
				Data14 = Data13[ADF_VER_TAM_int:]
				Data3, self.Ver_value = Shorten(Data14)
			else:
				self.Ver_value ='Não informado'
				self.ADF_VER_value = 'Não Informado'
				
				
			
		else:
			self.ADF_REF_value = 'AD Field Não informado'
			self.ADF_VER_value = 'Não informado'
			self.Ver_value = 'Não informado'
		if Data3[:2]=='80':
			Data10 = Cut_Str(Data3)
			UT_TAM = Data10[:2]
			Data11 =Cut_Str(Data10)
			Data3, self.UT_GUI_value = Shorten(Data11)
			Data3, self.UT_URL_value = Shorten(Data3)
			
		else:
			self.UT_GUI_value = 'Não informado'
			self.UT_URL_value = 'Não Informado'
		if Data3[:2] =='81':
			Data3 = Cut_Str(Data3)
			UTemp_TAM = Data3[:2]
			Data11 =Cut_Str(Data3)
			Data3, self.UT2_GUI_value = Shorten(Data11)
			Data3, self.UT2_OUT_value = Shorten(Data3)
		else:
			self.UT2_GUI_value = 'Não Informado'
			self.UT2_OUT_value = 'Não Informado'
		if Data3[:2] =='63':
			Data10 = Cut_Str(Data3)
			CRC_TAM = Data10[:2]
			CRC_TAM_int = int(CRC_TAM)
			Data11 = Cut_Str(Data10)
			self.CRC_value = Data11[:CRC_TAM_int]
		else:
			self.CRC_value ='Não informado'
