# from openpyxl.utils import get_column_letter, column_index_from_string
#
# from dtctest.config.config import *
# from dtctest.config import global_var

#创建Spy_Diag_Req_Msg函数
def build_Spy_Diag_Req_Msg_func() -> list:
	Spy_Diag_Req_Msg_func_List = []
	Spy_Diag_Req_Msg_func_List.append("void Spy_Diag_Req_Msg(GenericMessage * p_Msg, char index)\n")
	Spy_Diag_Req_Msg_func_List.append("{\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "if((p_Msg->btData[0] == 0x02) && (p_Msg->btData[1] == 0x10) && (p_Msg->btData[2] == 0x03))\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "{\n")
	Spy_Diag_Req_Msg_func_List.append("\t"*2 + "DiagReqFlag_1003[index] += 8;\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "}\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "else if((p_Msg->btData[0] == 0x04) && (p_Msg->btData[1] == 0x14) && (p_Msg->btData[2] == 0xFF)&& (p_Msg->btData[3] == 0xFF)&& (p_Msg->btData[4] == 0xFF))\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "{\n")
	Spy_Diag_Req_Msg_func_List.append("\t"*2 + "DiagReqFlag_14[index] += 8;\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "}\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "else if((p_Msg->btData[0] == 0x06) && (p_Msg->btData[1] == 0x19) && (p_Msg->btData[2] == 0x04) \\\n")
	Spy_Diag_Req_Msg_func_List.append("\t"*2 + "&& (p_Msg->btData[3] == DTC[index][0]) && (p_Msg->btData[4] == DTC[index][1]) && (p_Msg->btData[5] == DTC[index][2]) && (p_Msg->btData[6] == 0xFF))\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "{\n")
	Spy_Diag_Req_Msg_func_List.append("\t"*2 + "DiagReqFlag_1904[index] += 8;\n")
	Spy_Diag_Req_Msg_func_List.append("\t" + "}\n")
	Spy_Diag_Req_Msg_func_List.append("}\n")

	return Spy_Diag_Req_Msg_func_List

#创建Spy_Diag_Res_Msg函数
def build_Spy_Diag_Res_Msg_func() -> list:
	Spy_Diag_Res_Msg_func_List = []
	Spy_Diag_Res_Msg_func_List.append("void Spy_Diag_Res_Msg(GenericMessage * p_Msg, char index)\n")
	Spy_Diag_Res_Msg_func_List.append("{\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "if((p_Msg->btData[1] == 0x50) && (p_Msg->btData[2] == 0x03))\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "DiagResFlag_1003[index] += 1;\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "else if ((p_Msg->btData[0] == 0x01) && (p_Msg->btData[1] == 0x54))\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "DiagResFlag_14[index] += 1;\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "else if((p_Msg->btData[2] == 0x59) && (p_Msg->btData[3] == 0x04) \\\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "&& (p_Msg->btData[4] == DTC[index][0]) && (p_Msg->btData[5] == DTC[index][1]) && (p_Msg->btData[6] == DTC[index][2]))\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "if(p_Msg->btData[7] == 0x00)\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*3 + "DiagResFlag_1904_00[index] += 1;\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "else if(p_Msg->btData[7] == 0x2E)\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*3 + "DiagResFlag_1904_2E[index] += 1;\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "else if(p_Msg->btData[7] == 0x2F)\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*3 + "DiagResFlag_1904_2F[index] += 1;\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "else if((p_Msg->btData[1] == 0x59) && (p_Msg->btData[2] == 0x04) \\\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "&& (p_Msg->btData[3] == DTC[index][0]) && (p_Msg->btData[4] == DTC[index][1]) && (p_Msg->btData[5] == DTC[index][2]))\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "if(p_Msg->btData[6] == 0x00)\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*3 + "DiagResFlag_1904_00[index] += 1;\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "else if(p_Msg->btData[6] == 0x2E)\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*3 + "DiagResFlag_1904_2E[index] += 1;\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "else if(p_Msg->btData[6] == 0x2F)\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "{\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*3 + "DiagResFlag_1904_2F[index] += 1;\n")
	Spy_Diag_Res_Msg_func_List.append("\t"*2 + "}\n")
	Spy_Diag_Res_Msg_func_List.append("\t" + "}\n")
	Spy_Diag_Res_Msg_func_List.append("}\n")

	return Spy_Diag_Res_Msg_func_List

#创建Spy_TxRxMsg_Flag函数
def build_Spy_TxRxMsg_Flag_func() -> list:
	Spy_TxRxMsg_Flag_func_List = []
	Spy_TxRxMsg_Flag_func_List.append("void Spy_TxRxMsg_Flag(GenericMessage * p_Msg, char index)\n")
	Spy_TxRxMsg_Flag_func_List.append("{\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "if ((p_Msg->iNetwork == Msg[index].iNetwork) && (p_Msg->iID == Msg[index].iID))\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "{\n")
	Spy_TxRxMsg_Flag_func_List.append("\t"*2 + "MsgTxFlag[index] = 8;\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "}\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "if ((p_Msg->iNetwork == DiagCH) && (p_Msg->iID == Diag_Req_ID))\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "{\n")
	Spy_TxRxMsg_Flag_func_List.append("\t"*2 + "Spy_Diag_Req_Msg(p_Msg, index);\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "}\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "if((p_Msg->iNetwork == DiagCH) && (p_Msg->iID == Diag_Res_ID))\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "{\n")
	Spy_TxRxMsg_Flag_func_List.append("\t"*2 + "Spy_Diag_Res_Msg(p_Msg, index);\n")
	Spy_TxRxMsg_Flag_func_List.append("\t" + "}\n")
	Spy_TxRxMsg_Flag_func_List.append("}\n")

	return Spy_TxRxMsg_Flag_func_List

#创建Spy_EveryMessage函数
def build_Spy_EveryMessage_func() -> list:
	Spy_EveryMessage_func_List = []
	Spy_EveryMessage_func_List.append("void Spy_EveryMessage(GenericMessage * p_Msg)\n")
	Spy_EveryMessage_func_List.append("{\n")
	Spy_EveryMessage_func_List.append("\t" + "// TODO: add something you want to do for every message\n")
	Spy_EveryMessage_func_List.append("\t" + "char index = 0;\n")
	Spy_EveryMessage_func_List.append("\t" + "for(index=0; index < Num_DTC; index++)\n")
	Spy_EveryMessage_func_List.append("\t" + "{\n")
	Spy_EveryMessage_func_List.append("\t"*2 + "if(MsgTestEnable[index])\n")
	Spy_EveryMessage_func_List.append("\t"*2 + "{\n")
	Spy_EveryMessage_func_List.append("\t"*3 + "Spy_TxRxMsg_Flag(p_Msg, index);\n")
	Spy_EveryMessage_func_List.append("\t"*2 + "}\n")
	Spy_EveryMessage_func_List.append("\t" + "}\n")
	Spy_EveryMessage_func_List.append("\t" + "//printf(" + "Spy_EveryMessage" + ");\n")
	Spy_EveryMessage_func_List.append("}\n")

	return Spy_EveryMessage_func_List


#创建Spy_TxMsg函数
def build_Spy_TxMsg_func() -> list:
	Spy_TxMsg_func_List = []
	Spy_TxMsg_func_List.append("void Spy_TxMsg(char index)\n")
	Spy_TxMsg_func_List.append("{\n")
	Spy_TxMsg_func_List.append("\t" + "LoopCount[index] += 3;\n")
	Spy_TxMsg_func_List.append("\t" + "if(MsgTxEnable[index] && (LoopCount[index] >= MsgPeriod[index]))\n")
	Spy_TxMsg_func_List.append("\t" + "{\n")
	Spy_TxMsg_func_List.append("\t"*2 + "GenericMessageTransmit(&Msg[index]);\n")
	Spy_TxMsg_func_List.append("\t"*2 + "LoopCount[index] = 0;\n")
	Spy_TxMsg_func_List.append("\t" + "}\n")
	Spy_TxMsg_func_List.append("}\n")

	return Spy_TxMsg_func_List

#创建Spy_EveryLoop函数
def build_Spy_EveryLoop_func() -> list:
	Spy_EveryLoop_func_List = []
	Spy_EveryLoop_func_List.append("void Spy_EveryLoop(unsigned int uiCurrentTime)\n")
	Spy_EveryLoop_func_List.append("{\n")
	Spy_EveryLoop_func_List.append("\t" + "// TODO: add something you want to do every millisecond\n")
	Spy_EveryLoop_func_List.append("\t" + "char index = 0;\n")
	Spy_EveryLoop_func_List.append("\t" + "for(index=0; index < Num_DTC; index++)\n")
	Spy_EveryLoop_func_List.append("\t" + "{\n")
	Spy_EveryLoop_func_List.append("\t"*2 + "if(MsgTestEnable[index])\n")
	Spy_EveryLoop_func_List.append("\t"*2 + "{\n")
	Spy_EveryLoop_func_List.append("\t"*3 + "Spy_TxMsg(index);\n")
	Spy_EveryLoop_func_List.append("\t"*2 + "}\n")
	Spy_EveryLoop_func_List.append("\t" + "}\n")
	Spy_EveryLoop_func_List.append("\t" + "//printf(" + '"' + r"%lld\n" + '"' + ",uiCurrentTime);\n")
	Spy_EveryLoop_func_List.append("}\n")

	return Spy_EveryLoop_func_List

#创建printlog函数
def build_printlog_func() -> list:
	printlog_func_List = []
	printlog_func_List.append("void printlog(char index)\n")
	printlog_func_List.append("{\n")
	printlog_func_List.append("\t" + "if(MsgTxFlag[index] && (DiagReqFlag_1003[index] == 8) && (DiagResFlag_1003[index] == 1) && (DiagReqFlag_14[index] == 8) && (DiagResFlag_14[index] == 1)\n")
	printlog_func_List.append("\t" + "&& (DiagReqFlag_1904[index] == 24) && (DiagResFlag_1904_00[index] == 1) && (DiagResFlag_1904_2F[index] == 1) && (DiagResFlag_1904_2E[index] == 1))\n")
	printlog_func_List.append("\t" + "{\n")
	printlog_func_List.append("\t"*2 + "printf(" + '"' + r"%.2X%.2X%.2X Test OK!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t" + "}\n")
	printlog_func_List.append("\t" + "else\n")
	printlog_func_List.append("\t" + "{\n")
	printlog_func_List.append("\t"*2 + "if(MsgTxFlag[index])\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"0x%.3X Tx OK!" + '"' + ", Msg[index].iID);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"0x%.3X Tx Fail!" + '"' + ", Msg[index].iID);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"          %d" + '"' + ", MsgTxFlag[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t"*2 + "if(DiagReqFlag_1003[index] == 8)\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"10 03 Tx OK!" + '"' + ");\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"10 03 Tx Fail!" + '"' + ");\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"           %d" + '"' + ", DiagReqFlag_1003[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t"*2 + "if(DiagResFlag_1003[index] == 1)\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"10 03 Test OK!" + '"' + ");\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"10 03 Test Fail!" + '"' + ");\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"           %d" + '"' + ", DiagResFlag_1003[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t"*2 + "if(DiagReqFlag_14[index] == 8)\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"14 FF FF FF Tx OK!" + '"' + ");\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"14 FF FF FF Tx Fail!" + '"' + ");\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"           %d" + '"' + ", DiagReqFlag_14[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t"*2 + "if(DiagResFlag_14[index] == 1)\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"14 FF FF FF Test OK!" + '"' + ");\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"14 FF FF FF Test Fail!" + '"' + ");\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"           %d" + '"' + ", DiagResFlag_14[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t"*2 + "if(DiagReqFlag_1904[index] == 24)\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"19 04 %.2X %.2X %.2X FF Tx OK!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"19 04 %.2X %.2X %.2X FF Tx Fail!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"           %d" + '"' + ", DiagReqFlag_1904[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t"*2 + "if(DiagResFlag_1904_00[index] == 1)\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"59 04 %.2X %.2X %.2X 00 Test OK!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"59 04 %.2X %.2X %.2X 00 Test Fail!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"           %d" + '"' + ", DiagResFlag_1904_00[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t"*2 + "if(DiagResFlag_1904_2F[index] == 1)\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"59 04 %.2X %.2X %.2X 2F Test OK!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"59 04 %.2X %.2X %.2X 2F Test Fail!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"           %d" + '"' + ", DiagResFlag_1904_2F[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t"*2 + "if(DiagResFlag_1904_2E[index] == 1)\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"59 04 %.2X %.2X %.2X 2E Test OK!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t"*2 + "else\n")
	printlog_func_List.append("\t"*2 + "{\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"59 04 %.2X %.2X %.2X 2E Test Fail!" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + r"           %d" + '"' + ", DiagResFlag_1904_2E[index]);\n")
	printlog_func_List.append("\t"*3 + "printf(" + '"' + "          " + '"' + ");\n")
	printlog_func_List.append("\t"*2 + "}\n")
	printlog_func_List.append("\t" + "}\n")
	printlog_func_List.append("\n")

	printlog_func_List.append("\t" + "printf(" + '"' + r"\n" + '"' + ");\n")

	printlog_func_List.append("}\n")

	return printlog_func_List

#创建write2txt函数
def build_write2txt_func() -> list:
	write2txt_func_List = []
	write2txt_func_List.append("int write2txt(void)\n")
	write2txt_func_List.append("{\n")
	write2txt_func_List.append("\t" + "int index;\n")
	write2txt_func_List.append("\t" + "FILE *fpWrite = fopen(DATAPATHNAME," + '"' + "w" + '"' + ");\n")
	write2txt_func_List.append("\t" + "if(fpWrite == NULL)\n")
	write2txt_func_List.append("\t"*2 + "return 0;\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t" + "for(index = 0; index < Num_DTC; index++)\n")
	write2txt_func_List.append("\t" + "{\n")
	write2txt_func_List.append("\t"*2 + "if(MsgTxFlag[index])\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"0x%.3X Tx OK!\n" + '"' + ", Msg[index].iID);\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"0x%.3X Tx Fail!\n" + '"' + ", Msg[index].iID);\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "if(DiagReqFlag_1003[index] == 8)\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"10 03 Tx OK!\n" + '"' + ");\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"10 03 Tx Fail!\n" + '"' + ");\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "if(DiagResFlag_1003[index] == 1)\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"10 03 Test OK!\n" + '"' + ");\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"10 03 Test Fail!\n" + '"' + ");\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "if(DiagReqFlag_14[index] == 8)\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"14 FF FF FF Tx OK!\n" + '"' + ");\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"14 FF FF FF Tx Fail!\n" + '"' + ");\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "if(DiagResFlag_14[index] == 1)\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"14 FF FF FF Test OK!\n" + '"' + ");\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"14 FF FF FF Test Fail!\n" + '"' + ");\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "if(DiagReqFlag_1904[index] == 8*3)\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"19 04 %.2X %.2X %.2X FF Tx OK!\n" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"19 04 %.2X %.2X %.2X FF Tx Fail!\n" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "if(DiagResFlag_1904_00[index] == 1)\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"59 04 %.2X %.2X %.2X 00 Test OK!\n" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"59 04 %.2X %.2X %.2X 00 Test Fail!\n" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "if(DiagResFlag_1904_2F[index] == 1)\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"59 04 %.2X %.2X %.2X 2F Test OK!\n" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"59 04 %.2X %.2X %.2X 2F Test Fail!\n" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "if(DiagResFlag_1904_2E[index] == 1)\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"59 04 %.2X %.2X %.2X 2E Test OK!\n" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	write2txt_func_List.append("\t"*2 + "else\n")
	write2txt_func_List.append("\t"*3 + "fprintf(fpWrite, " + '"' + r"59 04 %.2X %.2X %.2X 2E Test Fail!\n" + '"' + ", DTC[index][0], DTC[index][1], DTC[index][2]);\n")
	write2txt_func_List.append("\n")

	write2txt_func_List.append("\t"*2 + "fprintf(fpWrite, " + '"' + r"\n\n" + '"' + ");\n")
	write2txt_func_List.append("\t" + "}\n")
	write2txt_func_List.append("\t" + "fclose(fpWrite);\n")
	write2txt_func_List.append("\t" + "return 1;\n")
	write2txt_func_List.append("}\n")

	return write2txt_func_List

#创建Spy_DTC_Test函数
def build_Spy_DTC_Test_func() -> list:
	Spy_DTC_Test_func_List = []
	Spy_DTC_Test_func_List.append("void Spy_DTC_Test(char index)\n")
	Spy_DTC_Test_func_List.append("{\n")
	Spy_DTC_Test_func_List.append("\t" + "MsgTestEnable[index] = 1;\n")
	Spy_DTC_Test_func_List.append("\t" + "MsgTxEnable[index] = 1;\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep((MsgPeriod[index] + MsgPeriod[index] + 1)*5);\n")
	Spy_DTC_Test_func_List.append("\t" + "GenericMessageTransmit(&Msg_76F_10_03);\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep(500);\n")
	Spy_DTC_Test_func_List.append("\t" + "GenericMessageTransmit(&Msg_76F_14);\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep(500);\n")
	Spy_DTC_Test_func_List.append("\t" + "GenericMessageTransmit(&Msg_76F_19_04[index]);\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep(500);\n")
	Spy_DTC_Test_func_List.append("\t" + "MsgTxEnable[index] = 0;\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep(MsgPeriod[index]*(ReportDTCCycle+2)*2);\n")
	Spy_DTC_Test_func_List.append("\t" + "GenericMessageTransmit(&Msg_76F_19_04[index]);\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep(500);\n")
	Spy_DTC_Test_func_List.append("\t" + "MsgTxEnable[index] = 1;\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep(500);\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep((MsgPeriod[index] + MsgPeriod[index] + 1)*5);\n")
	Spy_DTC_Test_func_List.append("\t" + "GenericMessageTransmit(&Msg_76F_19_04[index]);\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep(500);\n")
	Spy_DTC_Test_func_List.append("\t" + "MsgTxEnable[index] = 0;\n")
	Spy_DTC_Test_func_List.append("\t" + "MsgTestEnable[index] = 0;\n")
	Spy_DTC_Test_func_List.append("\t" + "Sleep(1000);\n")
	Spy_DTC_Test_func_List.append("}\n")

	return Spy_DTC_Test_func_List

#创建Spy_Main函数
def build_Spy_Main_func() -> list:
	Spy_Main_func_List = []
	Spy_Main_func_List.append("void Spy_Main()\n")
	Spy_Main_func_List.append("{\n")
	Spy_Main_func_List.append("\t" + "// TODO: Add code here to run every time Spy is run\n")
	Spy_Main_func_List.append("\t" + "char index = 0;\n")
	Spy_Main_func_List.append("\t" + "// delay for one second\n")
	Spy_Main_func_List.append("\t" + "Sleep(1000);\n")
	Spy_Main_func_List.append("\t" + "for(index = 0; index < Num_DTC; index++)\n")
	Spy_Main_func_List.append("\t" + "{\n")
	Spy_Main_func_List.append("\t"*2 + "Spy_DTC_Test(index);\n")
	Spy_Main_func_List.append("\t"*2 + "printlog(index);\n")
	Spy_Main_func_List.append("\t" + "}\n")
	Spy_Main_func_List.append("\t" + "if(write2txt())\n")
	Spy_Main_func_List.append("\t"*2 + "printf(" + '"' + r"Write to file success!\n" + '"' + ");\n")
	Spy_Main_func_List.append("\n")
	Spy_Main_func_List.append("\t" + "printf(" + '"' + r"--------------------END------------------------\n" + '"' + ");\n")
	Spy_Main_func_List.append("}\n")

	return Spy_Main_func_List






