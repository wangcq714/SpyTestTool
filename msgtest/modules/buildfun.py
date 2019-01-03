from openpyxl.utils import get_column_letter, column_index_from_string
# from msgtest.config.config import *
from msgtest.config import config
from msgtest.config import gv

#创建接收到的发送的单帧报文函数
def __build_SpyTxMsgFun(num) -> list:
	listtmp = []
	strtmp = "void SpyTxMsg_" + gv.ChannalMapping[gv.MessageData[num][column_index_from_string('F') - 1]] + '_' + 'N' + str(num) + '_' + str(gv.MessageData[num][column_index_from_string('A') - 1]) + "(GenericMessage *p_Msg)\n"
	strtmp += '{\n'
	strtmp += '\t' + 'MessageSendTime[' + str(num) + "] = p_Msg->iTimeStampNanoSecondsHW;\n"
	strtmp += '\t' + "MessageReceive[" + str(num) + '][' + str(config.Can2num[gv.ChannalMapping[gv.MessageData[num][column_index_from_string('F') - 1]]]-1) + "] += 8;\n"
	strtmp += '}\n'

	listtmp.append(strtmp)

	return listtmp
#创建接收到的发送的所有报文函数
def build_SpyTxMsgFun() -> list:
	SpyTxMsgFunList = []
	for i in range(len(gv.MessageData)):
		SpyTxMsgFunList.append(''.join(__build_SpyTxMsgFun(i)))
		SpyTxMsgFunList.append('\n')
	return SpyTxMsgFunList

#创建单帧报文接收处理函数
def __build_SpyMsgFun(num) -> list:

	listtmp = []
	for tmp in set(gv.MessageRxCH[num]):
		strtmp = "void SpyMsg_can" + str(tmp) + '_' + 'N' + str(num) + '_' + gv.MessageData[num][column_index_from_string('A') - 1] + "(GenericMessage *p_Msg)" + '\n'
		strtmp += '{' + '\n'
		strtmp += '\t' + "if" + '\n'
		strtmp += '\t' + '( ' + "p_Msg->btData[0] == 0x00 && p_Msg->btData[1] == 0x00 &&  p_Msg->btData[2] == 0x00 &&  p_Msg->btData[3] == 0x00 &&" + '\n'
		#strtmp += '\t'*2 + "p_Msg->btData[0] == 0x00 && p_Msg->btData[1] == 0x00 &&  p_Msg->btData[2] == 0x00 &&  p_Msg->btData[3] == 0x00 &&" + '\n'
		strtmp += '\t'*2 + "p_Msg->btData[4] == 0x00 && p_Msg->btData[5] == 0x00 &&  p_Msg->btData[6] == 0x00 &&  p_Msg->btData[7] == 0x00)" + '\n'
		strtmp += '\t' + '{' + '\n'
		strtmp += '\t'*2 + "if((p_Msg->iTimeStampNanoSecondsHW - MessageSendTime[" + str(num) + "]) > MessageTime[" + str(num) + "])" + '\n'
		strtmp += '\t'*2 + '{' + '\n'
		strtmp += '\t'*3 + "MessageTime[" + str(num) + "] = p_Msg->iTimeStampNanoSecondsHW - MessageSendTime[" + str(num) + "];" + '\n'
		strtmp += '\t'*2 + '}' + '\n'
		strtmp += '\t'*2 + "MessageReceive[" + str(num) + "][" + str(tmp-1) + "]++;" + '\n'
		strtmp += '\t' + '}' + '\n'
		strtmp += '\t' + "else" + '\n'
		strtmp += '\t' + '{' + '\n'
		strtmp += '\t'*2 + "MessageReceive[" + str(num) + "][" + str(tmp-1) + "] = -1;" + '\n'
		strtmp += '\t' + '}' + '\n'
		strtmp += '}' + '\n'
		listtmp.append(strtmp)

	return listtmp

#创建所有帧报文接收处理函数
def build_SpyMsgFun() -> list:
	SpyMsgFunList = []
	for i in range(len(gv.MessageData)):
		SpyMsgFunList.append(''.join(__build_SpyMsgFun(i)))
		SpyMsgFunList.append('\n')
	return SpyMsgFunList

#创建所有发送接收处理函数
def build_build_SpyTxRxMsgFun() -> list:
	SpyTxRxMsgFunList = []
	ist = []
	for i in range(len(gv.MessageData)):
		SpyTxRxMsgFunList.append(''.join(__build_SpyTxMsgFun(i)))
		SpyTxRxMsgFunList.append(''.join(__build_SpyMsgFun(i)))
		SpyTxRxMsgFunList.append('\n')
	return SpyTxRxMsgFunList

#创建判断发送函数
def __build_judgeTx(num) -> list:
	judgeTxList = []
	judgeTxstr = '\t'*2 + "if ((p_Msg->iNetwork == " + config.MessageTxCH2SpyCH[str(gv.MessageTxCH[num])] + ")&& (p_Msg->iID == " + gv.MessageData[num][column_index_from_string('A') - 1] + "))" + '\n'
	judgeTxstr += '\t'*2 + '{' + '\n'
	judgeTxstr += '\t'*3 + "SpyTxMsg_" + gv.ChannalMapping[gv.MessageData[num][column_index_from_string('F') - 1]] + '_' + 'N' +str(num) + '_' + gv.MessageData[num][column_index_from_string('A') - 1] + "(p_Msg);" + '\n'
	judgeTxstr += '\t'*2 + '}' + '\n'
	judgeTxList.append(judgeTxstr)

	return judgeTxstr

#创建判断接受函数
def __build_judgeRx(num) -> list:
	judgeRxList = []
	for i in set(gv.MessageRxCH[num]):
		judgeRxstr = '\t'*2 + "if ((p_Msg->iNetwork == " + config.MessageTxCH2SpyCH[str(i)] + ")&& (p_Msg->iID == " + gv.MessageData[num][column_index_from_string('A') - 1] + "))" + '\n'
		judgeRxstr += '\t'*2 + '{' + '\n'
		judgeRxstr += '\t'*3 + "SpyMsg_can" + str(i) + '_' + "N" + str(num) + '_' + gv.MessageData[num][column_index_from_string('A') - 1] + "(p_Msg);" + '\n'
		judgeRxstr += '\t'*2 + '}' + '\n'
		judgeRxList.append(judgeRxstr)

	return judgeRxList

#创建Spy_EveryMessageFun
def build_Spy_EveryMessageFun() -> list:
	Spy_EveryMessageFunList = [] 
	Spy_EveryMessageFunBeginstr = "void Spy_EveryMessage(GenericMessage * p_Msg)" + '\n'
	Spy_EveryMessageFunBeginstr += '{' + '\n'
	Spy_EveryMessageFunList.append(Spy_EveryMessageFunBeginstr)
	for i in range(len(gv.MessageData)):
		Spy_TxRxBeginstr = '\t' + "if(TxFlag[" + str(i) + "])" + '\n'
		Spy_TxRxBeginstr += '\t' + '{' + '\n'
		Spy_EveryMessageFunList.append(Spy_TxRxBeginstr)
		Spy_EveryMessageFunList.append(''.join(__build_judgeTx(i)))
		Spy_EveryMessageFunList.append(''.join(__build_judgeRx(i)))
		Spy_TxRxEndstr = '\t' + '}' + '\n'
		Spy_EveryMessageFunList.append(Spy_TxRxEndstr)
	Spy_EveryMessageFunEndstr = '}' + '\n'
	Spy_EveryMessageFunList.append(Spy_EveryMessageFunEndstr)
	Spy_EveryMessageFunList.append('\n')

	return Spy_EveryMessageFunList

#创建打印日志函数
def build_printlogFun() -> list:
	printlogFunlist = []
	printlogFunstr = "void printlog(unsigned int num)" + '\n'
	printlogFunstr += '{' + '\n'
	printlogFunstr += '\t' + "if( (MessageReceive[num][0] == MessageTransmit[num][0]) && (MessageReceive[num][1] == MessageTransmit[num][1])" + '\n'
	printlogFunstr += '\t' + "&&  (MessageReceive[num][2] == MessageTransmit[num][2]) && (MessageReceive[num][3] == MessageTransmit[num][3])" + '\n'
	printlogFunstr += '\t' + "&& (MessageReceive[num][4] == MessageTransmit[num][4]) &&  (MessageReceive[num][5] == MessageTransmit[num][5])" + '\n'
	printlogFunstr += '\t' + "&& (MessageReceive[num][6] == MessageTransmit[num][6]) &&  (MessageReceive[num][7] == MessageTransmit[num][7]))" + '\n'
	printlogFunstr += '{' + '\n'
	#printlogFunstr += '\t'*2 + "printf(" + '"' + "%s test success" + r'\n' + '"' + ", ID[num]);" + '\n'

	printlogFunstr += '\t'*2 + "if(strlen(ID[num]) == 5)" + '\n'
	printlogFunstr += '\t'*3 + "printf(" + '"' + "%s test success     " + '"' + ", ID[num]);" + '\n'
	printlogFunstr += '\t'*2 + "else" + '\n'
	printlogFunstr += '\t'*3 + "printf(" + '"' + "%s   test success     " + '"' + ", ID[num]);" + '\n'

	printlogFunstr += '\t'*2 + "printf(" + '"' + "DelayTime: %lld.%-3lldms" + '"' + ", MessageTime[num]/1000000,MessageTime[num]%1000000/1000);" + '\n'
	printlogFunstr += '\t' + '}' + '\n'
	printlogFunstr += '\t' + "else" + '\n'
	#printlogFunstr += '\t'*2 + "printf(" + '"' + "%s test fail" + r'\n' + '"' + ", ID[num]);" + '\n'
	printlogFunstr += '\t'*2 + "printf(" + '"' + "%s test fail" + '"' + ", ID[num]);" + '\n'
	printlogFunstr += '\t' + "if((num + 1) % 4 == 0)" + '\n'
	printlogFunstr += '\t'*2 + "printf(" + '"' + r'\n' + '"' + ");" '\n'
	printlogFunstr += '\t' + "else" + '\n'
	printlogFunstr += '\t'*2 + "printf(" + '"' + " "*10 + '"' + ");" + '\n'
	printlogFunstr += '}' + '\n'
	printlogFunlist.append(printlogFunstr)

	return printlogFunlist

def build_debugfun() -> list:
	build_debugList = []
	build_debugstr = "void printdebug(unsigned int num)" + '\n'
	build_debugstr += '{' + '\n'
	build_debugstr += '\t' + "int i = 0;" + '\n'
	build_debugstr += '\t' + "for(i=0; i<6; i++)" + '\n'
	build_debugstr += '\t' + '{' + '\n'
	build_debugstr += '\t'*2 + "printf(" + '"' + "%d, " + '"' + ",MessageReceive[num][i]);" + '\n'
	#build_debugstr += '\t'*2 + "printf(" + '"' + " "*5 + '"' + ");" + '\n'
	build_debugstr += '\t' + '}' + '\n'
	build_debugstr += '\t' + "printf(" + '"' + ' '*5 + '"' + ");" + '\n'
	build_debugstr += '\t' + "for(i=0; i<6; i++)" + '\n'
	build_debugstr += '\t' + '{' + '\n'
	build_debugstr += '\t'*2 + "printf(" + '"' + "%d, " + '"' + ",MessageTransmit[num][i]);" + '\n'
	#build_debugstr += '\t'*2 + "printf(" + '"' + " "*5 + '"' + ");" + '\n'
	build_debugstr += '\t' + '}' + '\n'
	build_debugstr += '\t' + "printf(" + '"' + ' '*5 + '"' + ");" + '\n'

	#build_debugstr += '\t' + "if(num%5 == 0)" + '\n'
	#build_debugstr += '\t'*2 + "printf(" + '"' + r'\n' + '"' + ");" '\n'
	#build_debugstr += '\t' + "else" + '\n'
	#build_debugstr += '\t'*2 + "printf(" + '"' + "     " + '"' + ");" + '\n'

	build_debugstr += '}' + '\n'
	build_debugList.append(build_debugstr)

	return build_debugList

#创建写入txt测试log函数
def build_write2txtfun() -> list:
	build_write2txtList = []
	build_write2txtStr = "int write2txt(void)" + '\n'
	build_write2txtStr += '{' + '\n'
	build_write2txtStr += '\t' + "int i;" + '\n'
	build_write2txtStr += '\t' + "FILE *fpWrite = fopen(DATAPATHNAME," + '"' + 'w' + '"' + ");" + '\n'
	build_write2txtStr += '\t' + "if(fpWrite == NULL)" + '\n'
	build_write2txtStr += '\t'*2 + "return 0;" + '\n'*2
	build_write2txtStr += '\t' + "for(i = 0; i < MessageQuantity; i++)" + '\n'
	build_write2txtStr += '\t' + '{' + '\n'
	build_write2txtStr += '\t'*2 + "if( (MessageReceive[i][0] == MessageTransmit[i][0]) && (MessageReceive[i][1] == MessageTransmit[i][1])" + '\n'
	build_write2txtStr += '\t'*3 + "&& (MessageReceive[i][2] == MessageTransmit[i][2]) && (MessageReceive[i][3] == MessageTransmit[i][3])" + '\n'
	build_write2txtStr += '\t'*3 + "&& (MessageReceive[i][4] == MessageTransmit[i][4]) && (MessageReceive[i][5] == MessageTransmit[i][5])" + '\n'
	build_write2txtStr += '\t'*3 + "&& (MessageReceive[i][6] == MessageTransmit[i][6]) && (MessageReceive[i][7] == MessageTransmit[i][7]))" + '\n'
	build_write2txtStr += '\t'*2 + '{' + '\n'
	build_write2txtStr += '\t'*3 + "if(strlen(ID[i]) == 5)" + '\n'
	build_write2txtStr += '\t'*4 + "fprintf(fpWrite, " + '"' + "%s test success     " + '"' + ", ID[i]);" + '\n'
	build_write2txtStr += '\t'*3 + "else" + '\n'
	build_write2txtStr += '\t'*4 + "fprintf(fpWrite, " + '"' + "%s  test success     " + '"' + ", ID[i]);" + '\n'
	build_write2txtStr += '\t'*3 + "fprintf(fpWrite, " + '"' + "DelayTime: %lld.%lldms" + '"' + ", MessageTime[i]/1000000,MessageTime[i]%1000000/1000);	" + '\n'
	build_write2txtStr += '\t'*2 + '}' + '\n'
	build_write2txtStr += '\t'*2 + "else" + '\n'
	build_write2txtStr += '\t'*2 + '{' + '\n'
	build_write2txtStr += '\t'*3 + "fprintf(fpWrite, " + '"' + "%s test fail" + '"' + ", ID[i]);" + '\n'
	build_write2txtStr += '\t'*2 + '}' + '\n'
	build_write2txtStr += '\t'*2 + "fprintf(fpWrite, " + '"' + r"\n" + '"' + ");" + '\n'
	build_write2txtStr += '\t' + '}' + '\n'
	build_write2txtStr += '\t' + "fclose(fpWrite);" + '\n'
	build_write2txtStr += '\t' + "return 1;" + '\n'
	build_write2txtStr += '}' + '\n'
	build_write2txtList.append(build_write2txtStr)
	return build_write2txtList



#创建发送报文函数
def __build_GenericMessageTransmitFun(num) -> list:
	build_GenericMessageTransmitFunList = []
	build_GenericMessageTransmitFunstr = "\t"*3 + "GenericMessageTransmit(&" +  'N' + str(num) + '_' +"Msg_" + gv.MessageData[num][0][2:] + ");" + '\n'
	build_GenericMessageTransmitFunstr += "\t"*3 + "Sleep(100);" + '\n'
	build_GenericMessageTransmitFunList.append(build_GenericMessageTransmitFunstr)

	return build_GenericMessageTransmitFunList

#创建调用打印Log函数
def __build_callprintlogFun(num) -> list:
	callprintlogFunList = []
	callprintlogFunstr = '\t' + "printlog(" + str(num) + ");" + '\n'
	callprintlogFunList.append(callprintlogFunstr)

	return callprintlogFunList

#创建调用调试函数
def __build_calldebugfun(num) -> list:
	calldebugFunList = []
	calldebugFunStr = '\t' + "printdebug(" + str(num) + ");" + '\n'
	calldebugFunList.append(calldebugFunStr)

	return calldebugFunList

def __build_call_write2txtfun() -> list:
	call_write2txtfunList = []
	call_write2txtfunStr = '\t' + "if(write2txt())" + '\n'
	call_write2txtfunStr += '\t'*2 + "printf(" + '"' + "write data.txt succss" + r"\n" + '"' + ");" + '\n'
	call_write2txtfunList.append(call_write2txtfunStr)
	return call_write2txtfunList


#创建主函数
def build_Spy_Main() -> list:
	Spy_MainList = []
	Spy_Mainbeginstr = "void Spy_Main()" + '\n'
	Spy_Mainbeginstr += "{" + '\n'
	Spy_Mainbeginstr += '\t' + "do" + '\n'
	Spy_Mainbeginstr += '\t' + '{' + '\n'
	Spy_MainList.append(Spy_Mainbeginstr)
	for i in range(len(gv.MessageData)):
		MessageTransmitFunBeginstr = '\t'*2 + "if(TxFlag[" + str(i) + "] == 0)" + '\n'
		MessageTransmitFunBeginstr += '\t'*2 + '{' + '\n'
		if i == 0:
			MessageTransmitFunBeginstr += '\t'*3 + "TxFlag[" + str(i) + "] = 1;" + '\n'
		else:
			MessageTransmitFunBeginstr += '\t'*3 + "TxFlag[" + str(i - 1) + "] = 0;" + '\n'
			MessageTransmitFunBeginstr += '\t'*3 + "TxFlag[" + str(i) + "] = 1;" + '\n'
		Spy_MainList.append(MessageTransmitFunBeginstr)
		Spy_MainList.append(''.join(__build_GenericMessageTransmitFun(i)))
		MessageTransmitFunEndstr = '\t'*2 + '}' + '\n'
		Spy_MainList.append(MessageTransmitFunEndstr)
	Spy_Mainmidstr = "\t"*2 +  "TxFlag[" + str(i) + "] = 0;" + '\n'
	Spy_Mainmidstr += "\t"*2 + "break;" + '\n'
	Spy_Mainmidstr += "\t" + "} while (1);" + '\n'
	Spy_MainList.append(Spy_Mainmidstr)
	for j in range(len(gv.MessageData)):
		Spy_MainList.append(''.join(__build_calldebugfun(j)))
		Spy_MainList.append(''.join(__build_callprintlogFun(j)))
	Spy_Mainmidstr = '\t' + "printf(" + '"' + r"\n" + '"' + ");" + '\n'
	Spy_MainList.append(Spy_Mainmidstr)
	Spy_MainList.append(''.join(__build_call_write2txtfun()))
	Spy_MainEndstr = '\t' + "printf(" + '"' + "--------------------END------------------------" + r'\n' + '"' + ");" + '\n'
	Spy_MainEndstr += '}' + '\n'
	Spy_MainList.append(Spy_MainEndstr)

	return Spy_MainList



