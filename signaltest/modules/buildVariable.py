from openpyxl.utils import get_column_letter, column_index_from_string
import sys
from signaltest.config import config
from signaltest.config import g_var


#创建Dest_Signal_Type结构体
def build_Dest_Signal_Type_struct() -> list:
	Dest_Signal_Type_struct_list = []
	Dest_Signal_Type_struct_list.append("typedef struct\n")
	Dest_Signal_Type_struct_list.append("{\n")
	Dest_Signal_Type_struct_list.append('\t' + "unsigned int Network;\n")
	Dest_Signal_Type_struct_list.append('\t' + "unsigned int Dest_ID;\n")
	Dest_Signal_Type_struct_list.append('\t' + "unsigned int period;\n")
	Dest_Signal_Type_struct_list.append('\t' + "unsigned int Data[3][8]; //Data[0]：Default; Data[1]：SourceSignal == 0; Data[2]：SourceSignal == 1.\n")
	Dest_Signal_Type_struct_list.append("}Dest_Signal_Type;\n")

	return Dest_Signal_Type_struct_list

#创建Test_Num变量
def build_Test_Num_var() -> list:
	Test_Num_var_list = []
	Test_Num_var_list.append("unsigned int Test_Num = 65535;\n")

	return Test_Num_var_list

#创建Source_SignalPeriod数组元素
def build_Source_SignalPeriod_Array_element(index) -> str:
	Source_SignalPeriod_Array_element_str = g_var.SignalDatas[index][column_index_from_string('G') - 1].strip(' ')
	Source_SignalPeriod_Array_element_str += ", "

	return Source_SignalPeriod_Array_element_str


#创建Source_SignalPeriod数组变量
def build_Source_SignalPeriod_Array() -> list:
	Source_SignalPeriod_Array_list = []
	Source_SignalPeriod_Array_list.append("unsigned int Source_SignalPeriod[Num_Signal] =\n")
	Source_SignalPeriod_Array_list.append('{\n')
	Source_SignalPeriod_Array_list.append('\t')
	for i in range(g_var.Num_Signal):
		Source_SignalPeriod_Array_list.append(build_Source_SignalPeriod_Array_element(i))
		if (i + 1)%10 == 0:
			Source_SignalPeriod_Array_list.append('\n\t')
	Source_SignalPeriod_Array_list.append('\n')
	Source_SignalPeriod_Array_list.append('};\n')

	return Source_SignalPeriod_Array_list

#计算信号值
def calc_signaVal(signalVal, startByte, startBit, signalLen, byteorder) -> list:
	signalData = [0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(int(signalLen)):
		if int(byteorder) == 0:
			signalData[int(startByte) - (int(startBit) + i)//8] |= (((int(signalVal, 16) >> i) & 0x01) << ((int(startBit) + i) % 8))
		elif int(byteorder) == 1:
			signalData[int(startByte) + (int(startBit) + i)//8] |= (((int(signalVal, 16) >> i) & 0x01) << ((int(startBit) + i) % 8))
	retData = [hex(x) for x in signalData]

	return retData


#创建目的信号默认值
def __build_DestSignal_default_val(index) -> str:
	DestSignal_default_val_str = '{'
	DestSignal_default_val_str += ', '.join(calc_signaVal(g_var.SignalDatas[index][column_index_from_string('D') - 1].strip(' '), \
														  g_var.SignalDatas[index][column_index_from_string('Q') - 1].strip(' '), \
														  g_var.SignalDatas[index][column_index_from_string('R') - 1].strip(' '), \
														  g_var.SignalDatas[index][column_index_from_string('S') - 1].strip(' '), \
														  g_var.SignalDatas[index][column_index_from_string('T') - 1].strip(' ')))
	DestSignal_default_val_str += '}'

	return DestSignal_default_val_str

#创建当源信号值等于0时目的信号值
def __build_DestSignal_val_scrVal0(index) -> str:
	build_DestSignal_val_scrVal0_str = '{'
	build_DestSignal_val_scrVal0_str += ', '.join(calc_signaVal('0x0', \
															    g_var.SignalDatas[index][column_index_from_string('Q') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('R') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('S') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('T') - 1].strip(' ')))
	build_DestSignal_val_scrVal0_str += '}'

	return build_DestSignal_val_scrVal0_str

#创建当源信号值等于1时目的信号值
def __build_DestSignal_val_scrVal1(index) -> str:
	build_DestSignal_val_scrVal1_str = '{'
	build_DestSignal_val_scrVal1_str += ', '.join(calc_signaVal(hex(int(("0b" + '1'*int(g_var.SignalDatas[index][column_index_from_string('S') - 1].strip(' '))), 2)), \
															    g_var.SignalDatas[index][column_index_from_string('Q') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('R') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('S') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('T') - 1].strip(' ')))
	build_DestSignal_val_scrVal1_str += '}'

	return build_DestSignal_val_scrVal1_str


#创建DestSignal数组元素
def __build_DestSignal_Array_Element(index: int) -> str:
	DestSignal_Array_Element_str = "{"
	DestSignal_Array_Element_str += config.MessageTxCH2SpyCH[str(config.Can2num[g_var.ChannalMapping[g_var.SignalDatas[index][column_index_from_string('N') - 1]]])] + ', '
	DestSignal_Array_Element_str += g_var.SignalDatas[index][column_index_from_string('M') - 1].strip(' ') + ', '
	DestSignal_Array_Element_str += g_var.SignalDatas[index][column_index_from_string('P') - 1].strip(' ') + ', '
	DestSignal_Array_Element_str += '{'
	DestSignal_Array_Element_str += __build_DestSignal_default_val(index)
	DestSignal_Array_Element_str += ", "
	DestSignal_Array_Element_str += __build_DestSignal_val_scrVal0(index)
	DestSignal_Array_Element_str += ", "
	DestSignal_Array_Element_str += __build_DestSignal_val_scrVal1(index)
	DestSignal_Array_Element_str += '}'
	DestSignal_Array_Element_str += '},'

	return DestSignal_Array_Element_str

#创建DestSignal数组变量
def build_DestSignal_Array() -> list:
	DestSignal_Array_list = []
	DestSignal_Array_list.append("Dest_Signal_Type DestSignal[Num_Signal] =\n")
	DestSignal_Array_list.append("{\n")
	for i in range(g_var.Num_Signal):
		DestSignal_Array_list.append('\t')
		DestSignal_Array_list.append(__build_DestSignal_Array_Element(i))
		DestSignal_Array_list.append('\n')

	DestSignal_Array_list.append("};\n")

	return DestSignal_Array_list

#创建DestSignalMask数组变量
def build_DestSignalMask_Array() -> list:
	DestSignalMask_Array_list = []
	DestSignalMask_Array_list.append("unsigned int DestSignalMask[Num_Signal][8] =\n")
	DestSignalMask_Array_list.append("{\n")
	for i in range(g_var.Num_Signal):
		DestSignalMask_Array_list.append('\t')
		DestSignalMask_Array_list.append(__build_DestSignal_val_scrVal1(i))
		DestSignalMask_Array_list.append(",\n")

	DestSignalMask_Array_list.append("};\n")

	return DestSignalMask_Array_list

#创建当源信号值等于0
def __build_SourceSignal_Value0(index) -> str:
	build_SourceSignal_Value0_str = '{'
	build_SourceSignal_Value0_str += ', '.join(calc_signaVal('0x0', \
															    g_var.SignalDatas[index][column_index_from_string('I') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('J') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('K') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('L') - 1].strip(' ')))
	build_SourceSignal_Value0_str += '}'

	return build_SourceSignal_Value0_str

#创建SourceSignal_Value0数组元素
def __build_SourceSignal_Value0_Array_element(index) -> str:
	SourceSignal_Value0_Array_element_str = '{'
	SourceSignal_Value0_Array_element_str += config.MessageTxCH2SpyCH[str(config.Can2num[g_var.ChannalMapping[g_var.SignalDatas[index][column_index_from_string('H') - 1]]])] + ', '
	SourceSignal_Value0_Array_element_str += g_var.SignalDatas[index][column_index_from_string('C') - 1].strip(' ') + ', '
	SourceSignal_Value0_Array_element_str += "0, "
	SourceSignal_Value0_Array_element_str += "0, "
	SourceSignal_Value0_Array_element_str += "8, "
	SourceSignal_Value0_Array_element_str += "0, "
	SourceSignal_Value0_Array_element_str += __build_SourceSignal_Value0(index)
	SourceSignal_Value0_Array_element_str += "},"

	return SourceSignal_Value0_Array_element_str

#创建SourceSignal_Value0数组变量
def build_SourceSignal_Value0_Array() -> list:
	SourceSignal_Value0_Array_list = []
	SourceSignal_Value0_Array_list.append("GenericMessage SourceSignal_Value0[Num_Signal] =\n")
	SourceSignal_Value0_Array_list.append("{\n")
	for i in range(g_var.Num_Signal):
		SourceSignal_Value0_Array_list.append("\t")
		SourceSignal_Value0_Array_list.append(__build_SourceSignal_Value0_Array_element(i))
		SourceSignal_Value0_Array_list.append("\n")

	SourceSignal_Value0_Array_list.append("};\n")

	return SourceSignal_Value0_Array_list

#创建当源信号值等于1
def __build_SourceSignal_Value1(index) -> str:
	build_SourceSignal_Value1_str = '{'
	build_SourceSignal_Value1_str += ', '.join(calc_signaVal(hex(int(("0b" + '1'*int(g_var.SignalDatas[index][column_index_from_string('K') - 1].strip(' '))), 2)), \
															    g_var.SignalDatas[index][column_index_from_string('I') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('J') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('K') - 1].strip(' '), \
															    g_var.SignalDatas[index][column_index_from_string('L') - 1].strip(' ')))
	build_SourceSignal_Value1_str += '}'

	return build_SourceSignal_Value1_str

#创建SourceSignal_Value0数组元素
def __build_SourceSignal_Value1_Array_element(index) -> str:
	SourceSignal_Value1_Array_element_str = '{'
	SourceSignal_Value1_Array_element_str += config.MessageTxCH2SpyCH[str(config.Can2num[g_var.ChannalMapping[g_var.SignalDatas[index][column_index_from_string('H') - 1]]])] + ', '
	SourceSignal_Value1_Array_element_str += g_var.SignalDatas[index][column_index_from_string('C') - 1].strip(' ') + ', '
	SourceSignal_Value1_Array_element_str += "0, "
	SourceSignal_Value1_Array_element_str += "0, "
	SourceSignal_Value1_Array_element_str += "8, "
	SourceSignal_Value1_Array_element_str += "0, "
	SourceSignal_Value1_Array_element_str += __build_SourceSignal_Value1(index)
	SourceSignal_Value1_Array_element_str += "},"

	return SourceSignal_Value1_Array_element_str


#创建SourceSignal_Value1数组变量
def build_SourceSignal_Value1_Array() -> list:
	SourceSignal_Value1_Array_list = []
	SourceSignal_Value1_Array_list.append("GenericMessage SourceSignal_Value1[Num_Signal] =\n")
	SourceSignal_Value1_Array_list.append("{\n")
	for i in range(g_var.Num_Signal):
		SourceSignal_Value1_Array_list.append("\t")
		SourceSignal_Value1_Array_list.append(__build_SourceSignal_Value1_Array_element(i))
		SourceSignal_Value1_Array_list.append("\n")

	SourceSignal_Value1_Array_list.append("};\n")

	return SourceSignal_Value1_Array_list

#创建TestEnable数组变量
def build_TestEnable_Array() -> list:
	TestEnable_Array_list = []
	TestEnable_Array_list.append("unsigned int SignalTestEnable[Num_Signal] = {0, };\n")
	TestEnable_Array_list.append("unsigned int SignalTest_Default_Begin_En[Num_Signal] = {0, };\n")
	TestEnable_Array_list.append("unsigned int SignalTest_Value0_En[Num_Signal] = {0, };\n")
	TestEnable_Array_list.append("unsigned int SignalTest_Value1_En[Num_Signal] = {0, };\n")
	TestEnable_Array_list.append("unsigned int SignalTest_Default_End_En[Num_Signal] = {0, };\n")

	return TestEnable_Array_list

#创建TestFlag数组变量
def build_TestFlag_Array() -> list:
	TestFlag_Array_list = []
	TestFlag_Array_list.append("unsigned int SourceSignal_Value0_Tx_Flag[Num_Signal] = {0, };\n")
	TestFlag_Array_list.append("unsigned int SourceSignal_Value1_Tx_Flag[Num_Signal] = {0, };\n")
	TestFlag_Array_list.append("unsigned int DestSignal_Default_Begin_Flag[Num_Signal] = {0, };\n")
	TestFlag_Array_list.append("unsigned int DestSignal_Value0_Flag[Num_Signal] = {0, };\n")
	TestFlag_Array_list.append("unsigned int DestSignal_Value1_Flag[Num_Signal] = {0, };\n")
	TestFlag_Array_list.append("unsigned int DestSignal_Default_End_Flag[Num_Signal] = {0, };\n")
	TestFlag_Array_list.append("unsigned int SamplingFlag[Num_Signal][6] = {0, };\n")

	return TestFlag_Array_list

#创建LoopCount数组变量
def build_LoopCount_Array() -> list:
	LoopCount_Array_list = []
	LoopCount_Array_list.append("unsigned int LoopCount[Num_Signal][2] = {0, };\n")

	return LoopCount_Array_list


