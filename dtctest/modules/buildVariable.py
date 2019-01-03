from openpyxl.utils import get_column_letter, column_index_from_string
import sys

from dtctest.config import global_var
from dtctest.config import config

#创建DTC数组元素
def __build_DTC_array_element(DTC_Code:str) -> str:
	DTC_array_element_Str = '{'
	DTC_array_element_Str += "0x" + DTC_Code[0:2] + ', '
	DTC_array_element_Str += "0x" + DTC_Code[2:4] + ', '
	DTC_array_element_Str += "0x" + DTC_Code[4:6]
	DTC_array_element_Str += "}, "

	return DTC_array_element_Str


#创建DTC数组
def build_DTC_array() -> list:
	DTC_array_List = []
	DTC_array_List.append("int DTC[Num_DTC][3] =\n")
	DTC_array_List.append("{\n\t")
	for i in range(global_var.Num_DTC):
		DTC_array_List.append(__build_DTC_array_element(global_var.DTC_Datas[i][column_index_from_string('E') - 1])) 
		if (i + 1) % 5 == 0:
			DTC_array_List.append('\n\t')
	DTC_array_List.append("\n")
	DTC_array_List.append("};\n")
	
	return DTC_array_List

#创建报文周期数组
def build_MsgPeriod_array() -> list:
	MsgPeriod_array_List = []
	MsgPeriod_array_List.append("int MsgPeriod[Num_DTC] = {")
	for i in range(global_var.Num_DTC):
		MsgPeriod_array_List.append(global_var.DTC_Datas[i][column_index_from_string('C') - 1] + ', ') 
	MsgPeriod_array_List.append("};\n")
	
	return MsgPeriod_array_List

#创建报告DTC周期
def build_ReportDTCCycle() -> list:
	ReportDTCCycle_List = []
	ReportDTCCycle_List.append("int ReportDTCCycle = 30;\n")
	
	return ReportDTCCycle_List

#创建报告DTC时间数组
def build_ReportDTCTimer_array() -> list:
	ReportDTCTimer_array_List = []
	ReportDTCTimer_array_List.append("int ReportDTCTimer[Num_DTC] = {0,};\n")
	
	return ReportDTCTimer_array_List

#创建清除DTC时间
def build_ClearDTCTimer() -> list:
	ClearDTCTimer_List = []
	ClearDTCTimer_List.append("int ClearDTCTimer = 1;\n")
	
	return ClearDTCTimer_List

#创建Msg测试使能数组
def build_MsgTestEnable_array() -> list:
	MsgTestEnable_array_List = []
	MsgTestEnable_array_List.append("int MsgTestEnable[Num_DTC] = {0,};\n")
	
	return MsgTestEnable_array_List

#创建Msg发送使能数组
def build_MsgTxEnable_array() -> list:
	MsgTxEnable_array_List = []
	MsgTxEnable_array_List.append("int MsgTxEnable[Num_DTC] = {0,};\n")
	
	return MsgTxEnable_array_List

#创建Msg发送标志数组
def build_MsgTxFlag_array() -> list:
	MsgTxFlag_array_List = []
	MsgTxFlag_array_List.append("int MsgTxFlag[Num_DTC] = {0,};\n")
	
	return MsgTxFlag_array_List

#创建诊断请求10 03标志数组
def build_DiagReqFlag_1003_array() -> list:
	DiagReqFlag_1003_array_List = []
	DiagReqFlag_1003_array_List.append("int DiagReqFlag_1003[Num_DTC] = {0,};\n")
	
	return DiagReqFlag_1003_array_List

#创建诊断响应10 03标志数组
def build_DiagResFlag_1003_array() -> list:
	DiagResFlag_1003_array_List = []
	DiagResFlag_1003_array_List.append("int DiagResFlag_1003[Num_DTC] = {0,};\n")
	
	return DiagResFlag_1003_array_List

#创建诊断请求14标志数组
def build_DiagReqFlag_14_array() -> list:
	DiagReqFlag_14_array_List = []
	DiagReqFlag_14_array_List.append("int DiagReqFlag_14[Num_DTC] = {0,};\n")
	
	return DiagReqFlag_14_array_List

#创建诊断响应14标志数组
def build_DiagResFlag_14_array() -> list:
	DiagResFlag_14_array_List = []
	DiagResFlag_14_array_List.append("int DiagResFlag_14[Num_DTC] = {0,};\n")
	
	return DiagResFlag_14_array_List

#创建诊断请求19 04标志数组
def build_DiagReqFlag_1904_array() -> list:
	DiagReqFlag_1904_array_List = []
	DiagReqFlag_1904_array_List.append("int DiagReqFlag_1904[Num_DTC] = {0,};\n")
	
	return DiagReqFlag_1904_array_List

#创建诊断响应19 04 xx xx xx 00标志数组
def build_DiagResFlag_1904_00_array() -> list:
	DiagResFlag_1904_00_array_List = []
	DiagResFlag_1904_00_array_List.append("int DiagResFlag_1904_00[Num_DTC] = {0,};\n")
	
	return DiagResFlag_1904_00_array_List

#创建诊断响应19 04 xx xx xx 2E标志数组
def build_DiagResFlag_1904_2E_array() -> list:
	DiagResFlag_1904_2E_array_List = []
	DiagResFlag_1904_2E_array_List.append("int DiagResFlag_1904_2E[Num_DTC] = {0,};\n")
	
	return DiagResFlag_1904_2E_array_List

#创建诊断响应19 04 xx xx xx 2F标志数组
def build_DiagResFlag_1904_2F_array() -> list:
	DiagResFlag_1904_2F_array_List = []
	DiagResFlag_1904_2F_array_List.append("int DiagResFlag_1904_2F[Num_DTC] = {0,};\n")
	
	return DiagResFlag_1904_2F_array_List

#创建周期函数循环计数数组
def build_LoopCount_array() -> list:
	LoopCount_array_List = []
	LoopCount_array_List.append("int LoopCount[Num_DTC] = {0,};\n")
	
	return LoopCount_array_List


#创建GenericMessage Msg_76F_10_03定义
def build_Msg_76F_10_03() -> list:
	Msg_76F_10_03_List = []
	Msg_76F_10_03_List.append("GenericMessage Msg_76F_10_03 = {DiagCH, Diag_Req_ID, 0, 0, 8, 0, {2, 0x10, 0x03, 0, 0, 0, 0, 0}};\n")

	return Msg_76F_10_03_List

#创建GenericMessage Msg_76F_14定义
def build_Msg_76F_14() -> list:
	Msg_76F_14_List = []
	Msg_76F_14_List.append("GenericMessage Msg_76F_14 = {DiagCH, Diag_Req_ID, 0, 0, 8, 0, {4, 0x14, 0xFF, 0xFF, 0xFF, 0, 0, 0}};\n")

	return Msg_76F_14_List

#创建GenericMessage Msg_76F_19_04数组元素
def __build_Msg_76F_19_04_element(DTC_Code:str) -> str:
	Msg_76F_19_04_element_Str = '{DiagCH, Diag_Req_ID, 0, 0, 8, 0, {6, 0x19, 0x04, '
	Msg_76F_19_04_element_Str += "0x" + DTC_Code[0:2] + ', '
	Msg_76F_19_04_element_Str += "0x" + DTC_Code[2:4] + ', '
	Msg_76F_19_04_element_Str += "0x" + DTC_Code[4:6] + ', '
	Msg_76F_19_04_element_Str += "0xFF, 0}},"
	Msg_76F_19_04_element_Str += "\n"

	return Msg_76F_19_04_element_Str

#创建GenericMessage Msg_76F_19_04数组定义
def build_Msg_76F_19_04_array() -> list:
	Msg_76F_19_04_List = []
	Msg_76F_19_04_List.append("GenericMessage Msg_76F_19_04[Num_DTC] =\n")
	Msg_76F_19_04_List.append("{\n")
	for i in range(global_var.Num_DTC):
		Msg_76F_19_04_List.append('\t')
		Msg_76F_19_04_List.append(__build_Msg_76F_19_04_element(global_var.DTC_Datas[i][column_index_from_string('E') - 1]))
	Msg_76F_19_04_List.append("};\n")

	return Msg_76F_19_04_List


#创建GenericMessage Msg元素数组
def __build_Msg_array_element(DTC_Data:list) -> str:
	Msg_array_element_Str = '{'
	Msg_array_element_Str += config.MessageTxCH2SpyCH[str(config.Can2num[global_var.ChannalMapping[DTC_Data[column_index_from_string('F') - 1].strip(' ')]])] + ', '
	Msg_array_element_Str += DTC_Data[column_index_from_string('A') - 1].strip(' ') + ', '
	Msg_array_element_Str += "0, 0, 8, 0, {1, 2, 3, 4, 5, 6, 7, 8}},\n"

	return Msg_array_element_Str


#创建GenericMessage Msg数组
def build_Msg_array() -> list:
	Msg_List = []
	Msg_List.append("GenericMessage Msg[Num_DTC] =\n")
	Msg_List.append("{\n")
	for i in range(global_var.Num_DTC):
		Msg_List.append('\t')
		Msg_List.append(__build_Msg_array_element(global_var.DTC_Datas[i]))
	Msg_List.append("};\n")

	return Msg_List
	

