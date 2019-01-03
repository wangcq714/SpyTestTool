from openpyxl.utils import get_column_letter, column_index_from_string
# from signaltest.config.config import *
# from signaltest.config import config
from signaltest.config import g_var

#创建SpyRxDestSignal函数
def build_SpyRxDestSignal_func() -> list:
	SpyRxDestSignal_func_list = []
	SpyRxDestSignal_func_list.append("void SpyRxDestSignal(unsigned int index, GenericMessage * p_Msg)\n")
	SpyRxDestSignal_func_list.append("{\n")
	SpyRxDestSignal_func_list.append('\t' + "if(SignalTest_Default_Begin_En[index])\n")
	SpyRxDestSignal_func_list.append('\t' + "{\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "if(SamplingFlag[index][0] == 1)\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "{\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "if(((p_Msg->btData[0]&DestSignalMask[index][0]) == (DestSignal[index].Data[0][0]&DestSignalMask[index][0]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[1]&DestSignalMask[index][1]) == (DestSignal[index].Data[0][1]&DestSignalMask[index][1]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[2]&DestSignalMask[index][2]) == (DestSignal[index].Data[0][2]&DestSignalMask[index][2]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[3]&DestSignalMask[index][3]) == (DestSignal[index].Data[0][3]&DestSignalMask[index][3]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[4]&DestSignalMask[index][4]) == (DestSignal[index].Data[0][4]&DestSignalMask[index][4]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[5]&DestSignalMask[index][5]) == (DestSignal[index].Data[0][5]&DestSignalMask[index][5]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[6]&DestSignalMask[index][6]) == (DestSignal[index].Data[0][6]&DestSignalMask[index][6]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[7]&DestSignalMask[index][7]) == (DestSignal[index].Data[0][7]&DestSignalMask[index][7])))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "{\n")
	SpyRxDestSignal_func_list.append('\t'*4 + "DestSignal_Default_Begin_Flag[index] += 1;\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "}\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "SamplingFlag[index][0] += 1;\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "}\n")
	SpyRxDestSignal_func_list.append('\t' + "}\n")
	SpyRxDestSignal_func_list.append('\t' + "else if(SignalTest_Value0_En[index])\n")
	SpyRxDestSignal_func_list.append('\t' + "{\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "if(SamplingFlag[index][1] == 1)\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "{\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "if(((p_Msg->btData[0]&DestSignalMask[index][0]) == (DestSignal[index].Data[1][0]&DestSignalMask[index][0]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[1]&DestSignalMask[index][1]) == (DestSignal[index].Data[1][1]&DestSignalMask[index][1]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[2]&DestSignalMask[index][2]) == (DestSignal[index].Data[1][2]&DestSignalMask[index][2]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[3]&DestSignalMask[index][3]) == (DestSignal[index].Data[1][3]&DestSignalMask[index][3]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[4]&DestSignalMask[index][4]) == (DestSignal[index].Data[1][4]&DestSignalMask[index][4]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[5]&DestSignalMask[index][5]) == (DestSignal[index].Data[1][5]&DestSignalMask[index][5]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[6]&DestSignalMask[index][6]) == (DestSignal[index].Data[1][6]&DestSignalMask[index][6]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[7]&DestSignalMask[index][7]) == (DestSignal[index].Data[1][7]&DestSignalMask[index][7])))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "{\n")
	SpyRxDestSignal_func_list.append('\t'*4 + "DestSignal_Value0_Flag[index] += 1;\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "}\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "SamplingFlag[index][1] += 1;\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "}\n")
	SpyRxDestSignal_func_list.append('\t' + "}\n")
	SpyRxDestSignal_func_list.append('\t' + "else if(SignalTest_Value1_En[index])\n")
	SpyRxDestSignal_func_list.append('\t' + "{\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "if(SamplingFlag[index][2] == 1)\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "{\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "if(((p_Msg->btData[0]&DestSignalMask[index][0]) == (DestSignal[index].Data[2][0]&DestSignalMask[index][0]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[1]&DestSignalMask[index][1]) == (DestSignal[index].Data[2][1]&DestSignalMask[index][1]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[2]&DestSignalMask[index][2]) == (DestSignal[index].Data[2][2]&DestSignalMask[index][2]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[3]&DestSignalMask[index][3]) == (DestSignal[index].Data[2][3]&DestSignalMask[index][3]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[4]&DestSignalMask[index][4]) == (DestSignal[index].Data[2][4]&DestSignalMask[index][4]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[5]&DestSignalMask[index][5]) == (DestSignal[index].Data[2][5]&DestSignalMask[index][5]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[6]&DestSignalMask[index][6]) == (DestSignal[index].Data[2][6]&DestSignalMask[index][6]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[7]&DestSignalMask[index][7]) == (DestSignal[index].Data[2][7]&DestSignalMask[index][7])))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "{\n")
	SpyRxDestSignal_func_list.append('\t'*4 + "DestSignal_Value1_Flag[index] += 1;\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "}\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "SamplingFlag[index][2] += 1;\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "}\n")
	SpyRxDestSignal_func_list.append('\t' + "}\n")
	SpyRxDestSignal_func_list.append('\t' + "else if(SignalTest_Default_End_En[index])\n")
	SpyRxDestSignal_func_list.append('\t' + "{\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "if(SamplingFlag[index][3] == 1)\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "{\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "if(((p_Msg->btData[0]&DestSignalMask[index][0]) == (DestSignal[index].Data[0][0]&DestSignalMask[index][0]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[1]&DestSignalMask[index][1]) == (DestSignal[index].Data[0][1]&DestSignalMask[index][1]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[2]&DestSignalMask[index][2]) == (DestSignal[index].Data[0][2]&DestSignalMask[index][2]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[3]&DestSignalMask[index][3]) == (DestSignal[index].Data[0][3]&DestSignalMask[index][3]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[4]&DestSignalMask[index][4]) == (DestSignal[index].Data[0][4]&DestSignalMask[index][4]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[5]&DestSignalMask[index][5]) == (DestSignal[index].Data[0][5]&DestSignalMask[index][5]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[6]&DestSignalMask[index][6]) == (DestSignal[index].Data[0][6]&DestSignalMask[index][6]))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "&& ((p_Msg->btData[7]&DestSignalMask[index][7]) == (DestSignal[index].Data[0][7]&DestSignalMask[index][7])))\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "{\n")
	SpyRxDestSignal_func_list.append('\t'*4 + "DestSignal_Default_End_Flag[index] += 1;\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "}\n")
	SpyRxDestSignal_func_list.append('\t'*3 + "SamplingFlag[index][3] += 1;\n")
	SpyRxDestSignal_func_list.append('\t'*2 + "}\n")
	SpyRxDestSignal_func_list.append('\t' + "}\n")
	SpyRxDestSignal_func_list.append("}\n")

	return SpyRxDestSignal_func_list

#创建SpyRxSignal函数
def build_SpyRxSignal_func() -> list:
	SpyRxSignal_func_list = []
	SpyRxSignal_func_list.append("void SpyRxSignal(unsigned int index, GenericMessage * p_Msg)\n")
	SpyRxSignal_func_list.append("{\n")
	SpyRxSignal_func_list.append('\t' + "if(((SamplingFlag[index][0] == 1) || (SamplingFlag[index][1] == 1) || (SamplingFlag[index][2] == 1) || (SamplingFlag[index][3] == 1))\n")
	SpyRxSignal_func_list.append('\t' + "&& (p_Msg->iNetwork == DestSignal[index].Network) && (p_Msg->iID == DestSignal[index].Dest_ID))\n")
	SpyRxSignal_func_list.append('\t' + "{\n")
	SpyRxSignal_func_list.append('\t'*2 + "SpyRxDestSignal(index, p_Msg);\n")
	SpyRxSignal_func_list.append('\t' + "}\n")
	SpyRxSignal_func_list.append('\t' + "else if((SamplingFlag[index][4] == 1) && (p_Msg->iNetwork == SourceSignal_Value0[index].iNetwork) && (p_Msg->iID == SourceSignal_Value0[index].iID))\n")
	SpyRxSignal_func_list.append('\t' + "{\n")
	SpyRxSignal_func_list.append('\t'*2 + "SourceSignal_Value0_Tx_Flag[index] += 1;\n")
	SpyRxSignal_func_list.append('\t'*2 + "SamplingFlag[index][4] += 1;\n")
	SpyRxSignal_func_list.append('\t' + "}\n")
	SpyRxSignal_func_list.append('\t' + "else if((SamplingFlag[index][5] == 1) && (p_Msg->iNetwork == SourceSignal_Value1[index].iNetwork) && (p_Msg->iID == SourceSignal_Value1[index].iID))\n")
	SpyRxSignal_func_list.append('\t' + "{\n")
	SpyRxSignal_func_list.append('\t'*2 + "SourceSignal_Value1_Tx_Flag[index] += 1;\n")
	SpyRxSignal_func_list.append('\t'*2 + "SamplingFlag[index][5] += 1;\n")
	SpyRxSignal_func_list.append('\t' + "}\n")
	SpyRxSignal_func_list.append("}\n")

	return SpyRxSignal_func_list

#创建Spy_EveryMessage函数
def build_Spy_EveryMessage_func() -> list:
	Spy_EveryMessage_func_list = []
	Spy_EveryMessage_func_list.append("void Spy_EveryMessage(GenericMessage * p_Msg)\n")
	Spy_EveryMessage_func_list.append("{\n")
	Spy_EveryMessage_func_list.append('\t' + "// TODO: add something you want to do for every message\n")
	Spy_EveryMessage_func_list.append('\t' + "if((Test_Num != 65535) && SignalTestEnable[Test_Num])\n")
	Spy_EveryMessage_func_list.append('\t' + "{\n")
	Spy_EveryMessage_func_list.append('\t'*2 + "SpyRxSignal(Test_Num, p_Msg);\n")
	Spy_EveryMessage_func_list.append('\t' + "}\n")
	Spy_EveryMessage_func_list.append("}\n")

	return Spy_EveryMessage_func_list

#创建SpyTxSignal函数
def build_SpyTxSignal_func() -> list:
	SpyTxSignal_func_list = []
	SpyTxSignal_func_list.append("void SpyTxSignal(unsigned int index)\n")
	SpyTxSignal_func_list.append("{\n")
	SpyTxSignal_func_list.append('\t' + "if(SignalTest_Value0_En[index])\n")
	SpyTxSignal_func_list.append('\t' + "{\n")
	SpyTxSignal_func_list.append('\t'*2 + "LoopCount[index][0] += 3;\n")
	SpyTxSignal_func_list.append('\t'*2 + "if(LoopCount[index][0] >= Source_SignalPeriod[index])\n")
	SpyTxSignal_func_list.append('\t'*2 + "{\n")
	SpyTxSignal_func_list.append('\t'*3 + "GenericMessageTransmit(&SourceSignal_Value0[index]);\n")
	SpyTxSignal_func_list.append('\t'*3 + "LoopCount[index][0] = 0;\n")
	SpyTxSignal_func_list.append('\t'*2 + "}\n")
	SpyTxSignal_func_list.append('\t' + "}\n")
	SpyTxSignal_func_list.append('\t' + "else if(SignalTest_Value1_En[index])\n")
	SpyTxSignal_func_list.append('\t' + "{\n")
	SpyTxSignal_func_list.append('\t'*2 + "LoopCount[index][1] += 3;\n")
	SpyTxSignal_func_list.append('\t'*2 + "if(LoopCount[index][1] >= Source_SignalPeriod[index])\n")
	SpyTxSignal_func_list.append('\t'*2 + "{\n")
	SpyTxSignal_func_list.append('\t'*3 + "GenericMessageTransmit(&SourceSignal_Value1[index]);\n")
	SpyTxSignal_func_list.append('\t'*3 + "LoopCount[index][1] = 0;\n")
	SpyTxSignal_func_list.append('\t'*2 + "}\n")
	SpyTxSignal_func_list.append('\t' + "}\n")
	SpyTxSignal_func_list.append("}\n")

	return SpyTxSignal_func_list

#创建Spy_EveryLoop函数
def build_Spy_EveryLoop_func() -> list:
	Spy_EveryLoop_func_list = []
	Spy_EveryLoop_func_list.append("void Spy_EveryLoop(unsigned int uiCurrentTime)\n")
	Spy_EveryLoop_func_list.append("{\n")
	Spy_EveryLoop_func_list.append('\t' + "// TODO: add something you want to do every millisecond\n")
	Spy_EveryLoop_func_list.append('\t' + "if((Test_Num != 65535) && SignalTestEnable[Test_Num])\n")
	Spy_EveryLoop_func_list.append('\t' + "{\n")
	Spy_EveryLoop_func_list.append('\t'*2 + "SpyTxSignal(Test_Num);\n")
	Spy_EveryLoop_func_list.append('\t' + "}\n")
	Spy_EveryLoop_func_list.append("}\n")

	return Spy_EveryLoop_func_list

#创建printlog函数
def build_printlog_func() -> list:
	printlog_func_list = []
	printlog_func_list.append("void printlog(unsigned int index)\n")
	printlog_func_list.append("{\n")
	printlog_func_list.append('\t' + "if((SourceSignal_Value0_Tx_Flag[index] == 1) && (SourceSignal_Value1_Tx_Flag[index] == 1)\n")
	printlog_func_list.append('\t' + "&& (DestSignal_Default_Begin_Flag[index] == 1) && (DestSignal_Value0_Flag[index] == 1) \n")
	printlog_func_list.append('\t' + "&& (DestSignal_Value1_Flag[index] == 1) && (DestSignal_Default_End_Flag[index] == 1))\n")
	printlog_func_list.append('\t' + "{\n")
	printlog_func_list.append('\t'*2 + "printf(" + '"' + r"No.%d Test OK!     \n" + '"' + ", index + 1);\n")
	printlog_func_list.append('\t'*2 + "//printf(" + '"' + "SrcSigVal0Tx: %d     " + '"' + ", SourceSignal_Value0_Tx_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "//printf(" + '"' + "SrcSigVal1Tx: %d     " + '"' + ", SourceSignal_Value1_Tx_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "// printf(" + '"' + "BeginDefault: %d     " + '"' + ", DestSignal_Default_Begin_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "// printf(" + '"' + "SetValue==0: %d     " + '"' + ", DestSignal_Value0_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "// printf(" + '"' + "SetValue==1: %d     " + '"' + ", DestSignal_Value1_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "// printf(" + '"' + r"EndDefault: %d\n" + '"' + ", DestSignal_Default_End_Flag[index]);\n")
	printlog_func_list.append('\t' + "}\n")
	printlog_func_list.append('\t' + "else\n")
	printlog_func_list.append('\t' + "{\n")
	printlog_func_list.append('\t'*2 + "printf(" + '"' + "No.%d Test Fail!     " + '"' + ", index + 1);\n")
	printlog_func_list.append('\t'*2 + "printf(" + '"' + "SrcSigVal0Tx: %d     " + '"' + ", SourceSignal_Value0_Tx_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "printf(" + '"' + "SrcSigVal1Tx: %d     " + '"' + ", SourceSignal_Value1_Tx_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "printf(" + '"' + "BeginDefault: %d     " + '"' + ", DestSignal_Default_Begin_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "printf(" + '"' + "SetValue==0: %d     " + '"' + ", DestSignal_Value0_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "printf(" + '"' + "SetValue==1: %d     " + '"' + ", DestSignal_Value1_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "printf(" + '"' + r"EndDefault: %d\n" + '"' + ", DestSignal_Default_End_Flag[index]);\n")
	printlog_func_list.append('\t'*2 + "//printf(" + '"' + r"%d\n" + '"' + ", SamplingFlag[index][4]);\n")
	printlog_func_list.append('\t'*2 + "//printf(" + '"' + r"%d\n" + '"' + ", SamplingFlag[index][5]);\n")
	printlog_func_list.append('\t' + "}\n")
	printlog_func_list.append("}\n")

	return printlog_func_list

#创建write2txt函数
def build_write2txt_func() -> list:
	write2txt_func_list = []
	write2txt_func_list.append("int write2txt(void)\n")
	write2txt_func_list.append("{\n")
	write2txt_func_list.append('\t' + "int index;\n")
	write2txt_func_list.append('\t' + "FILE *fpWrite = fopen(DATAPATHNAME," + '"' + "w" + '"' + ");\n")
	write2txt_func_list.append('\t' + "if(fpWrite == NULL)\n")
	write2txt_func_list.append('\t' + "return 0;\n")
	write2txt_func_list.append("\n")
	write2txt_func_list.append('\t' + "for(index = 0; index < Num_Signal; index++)\n")
	write2txt_func_list.append('\t' + "{\n")
	write2txt_func_list.append('\t'*2 + "if((SourceSignal_Value0_Tx_Flag[index] == 1) && (SourceSignal_Value1_Tx_Flag[index] == 1)\n")
	write2txt_func_list.append('\t'*2 + "&& (DestSignal_Default_Begin_Flag[index] == 1) && (DestSignal_Value0_Flag[index] == 1) \n")
	write2txt_func_list.append('\t'*2 + "&& (DestSignal_Value1_Flag[index] == 1) && (DestSignal_Default_End_Flag[index] == 1))\n")
	write2txt_func_list.append('\t'*2 + "{\n")
	write2txt_func_list.append('\t'*3 + "fprintf(fpWrite, " + '"' + r"No.%d Test OK!\n" + '"' + ", index + 1);\n")
	write2txt_func_list.append('\t'*3 + "//printf(" + '"' + "SrcSigVal0Tx: %d     " + '"' + ", SourceSignal_Value0_Tx_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "//printf(" + '"' + "SrcSigVal1Tx: %d     " + '"' + ", SourceSignal_Value1_Tx_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "// printf(" + '"' + "BeginDefault: %d     " + '"' + ", DestSignal_Default_Begin_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "// printf(" + '"' + "SetValue==0: %d     " + '"' + ", DestSignal_Value0_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "// printf(" + '"' + "SetValue==1: %d     " + '"' + ", DestSignal_Value1_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "// printf(" + '"' + r"EndDefault: %d\n" + '"' + ", DestSignal_Default_End_Flag[index]);\n")
	write2txt_func_list.append('\t'*2 + "}\n")
	write2txt_func_list.append('\t'*2 + "else\n")
	write2txt_func_list.append('\t'*2 + "{\n")
	write2txt_func_list.append('\t'*3 + "fprintf(fpWrite, " + '"' + "No.%d Test Fail!     " + '"' + ", index + 1);\n")
	write2txt_func_list.append('\t'*3 + "fprintf(fpWrite, " + '"' + "SrcSigVal0Tx: %d     " + '"' + ", SourceSignal_Value0_Tx_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "fprintf(fpWrite, " + '"' + "SrcSigVal1Tx: %d     " + '"' + ", SourceSignal_Value1_Tx_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "fprintf(fpWrite, " + '"' + "BeginDefault: %d     " + '"' + ", DestSignal_Default_Begin_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "fprintf(fpWrite, " + '"' + "SetValue==0: %d     " + '"' + ", DestSignal_Value0_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "fprintf(fpWrite, " + '"' + "SetValue==1: %d     " + '"' + ", DestSignal_Value1_Flag[index]);\n")
	write2txt_func_list.append('\t'*3 + "fprintf(fpWrite, " + '"' + r"EndDefault: %d\n" + '"' + ", DestSignal_Default_End_Flag[index]);\n")
	write2txt_func_list.append('\t'*2 + "}\n")
	write2txt_func_list.append('\t' + "}\n")
	write2txt_func_list.append('\t' + "fclose(fpWrite);\n")
	write2txt_func_list.append('\t' + "return 1;\n")
	write2txt_func_list.append("}\n")

	return write2txt_func_list

#创建Spy_Signal_Test函数
def build_Spy_Signal_Test_func() -> list:
	Spy_Signal_Test_func_list = []
	Spy_Signal_Test_func_list.append("void Spy_Signal_Test(unsigned int index)\n")
	Spy_Signal_Test_func_list.append("{\n")
	Spy_Signal_Test_func_list.append('\t' + "Test_Num = index;\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTestEnable[index] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTest_Default_Begin_En[index] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "Sleep(DestSignal[index].period * 5);\n")
	Spy_Signal_Test_func_list.append('\t' + "SamplingFlag[index][0] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "Sleep(DestSignal[index].period * 5);\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTest_Default_Begin_En[index] = 0;\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTest_Value0_En[index] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "Sleep(((Source_SignalPeriod[index] > DestSignal[index].period) ? Source_SignalPeriod[index] : DestSignal[index].period) * 5);\n")
	Spy_Signal_Test_func_list.append('\t' + "SamplingFlag[index][1] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "SamplingFlag[index][4] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "Sleep(((Source_SignalPeriod[index] > DestSignal[index].period) ? Source_SignalPeriod[index] : DestSignal[index].period) * 5);\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTest_Value0_En[index] = 0;\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTest_Value1_En[index] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "Sleep(((Source_SignalPeriod[index] > DestSignal[index].period) ? Source_SignalPeriod[index] : DestSignal[index].period) * 5);\n")
	Spy_Signal_Test_func_list.append('\t' + "SamplingFlag[index][2] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "SamplingFlag[index][5] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "Sleep(((Source_SignalPeriod[index] > DestSignal[index].period) ? Source_SignalPeriod[index] : DestSignal[index].period) * 5);\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTest_Value1_En[index] = 0;\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTest_Default_End_En[index] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "Sleep(Source_SignalPeriod[index] * 15);\n")
	Spy_Signal_Test_func_list.append('\t' + "SamplingFlag[index][3] = 1;\n")
	Spy_Signal_Test_func_list.append('\t' + "Sleep(Source_SignalPeriod[index] * 15);\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTest_Default_End_En[index] = 0;\n")
	Spy_Signal_Test_func_list.append('\t' + "SignalTestEnable[index] = 0;\n")
	Spy_Signal_Test_func_list.append("}\n")

	return Spy_Signal_Test_func_list

#创建Spy_Main函数
def build_Spy_Main_func() -> list:
	Spy_Main_func_list = []
	Spy_Main_func_list.append("void Spy_Main()\n")
	Spy_Main_func_list.append("{\n")
	Spy_Main_func_list.append('\t' + "// TODO: Add code here to run every time Spy is run\n")
	Spy_Main_func_list.append('\t' + "unsigned int index = 0;\n")
	Spy_Main_func_list.append('\t' + "for(index = 0; index < Num_Signal; index++)\n")
	Spy_Main_func_list.append('\t' + "{\n")
	Spy_Main_func_list.append('\t'*2 + "Sleep(1000);\n")
	Spy_Main_func_list.append('\t'*2 + "Spy_Signal_Test(index);\n")
	Spy_Main_func_list.append('\t'*2 + "printlog(index);\n")
	Spy_Main_func_list.append('\t' + "}\n")
	Spy_Main_func_list.append("\n")
	Spy_Main_func_list.append('\t' + "if(write2txt())\n")
	Spy_Main_func_list.append('\t'*2 + "printf(" + '"' + r"Write to file success!\n" + '"' + ");\n")
	Spy_Main_func_list.append("\n")
	Spy_Main_func_list.append('\t' + "printf(" + '"' + r"--------------------END------------------------\n" + '"' + ");\n")
	Spy_Main_func_list.append("}\n")

	return Spy_Main_func_list





