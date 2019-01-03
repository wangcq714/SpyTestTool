from openpyxl.utils import get_column_letter, column_index_from_string
import sys
# from msgtest.config.config import *
from msgtest.config import config
from msgtest.config import gv

#生成单个报文发送通道标志，供内部调用
def __buildTxRxCHArray(num) -> str:
	tmplist = ['0', '0', '0', '0', '0', '0']
	tmpRxCH = []
	strtmp = "{"
	Txch = config.Can2num[gv.ChannalMapping[gv.MessageData[num][column_index_from_string('F') - 1]]]
	tmplist[ Txch- 1] = '8'
	gv.MessageTxCH.append(Txch)
	i = 0
	for tick in gv.MessageData[num][column_index_from_string('L') - 1 : column_index_from_string('G') -2 : -1]:
		if tick.find('√') != -1:
			tmplist[i] = '1'
			tmpRxCH.append(i + 1)
		i += 1
	gv.MessageRxCH.append(tmpRxCH)
	strtmp += ','.join(tmplist)
	strtmp += "}, "
	return strtmp


#生成单个报文发送通道标志，供内部调用(克隆)
def __buildTxRxCHArrayClone(num) -> str:
	tmplist = ['0', '0', '0', '0', '0', '0']
	tmpRxCH = []
	strtmp = "{"
	Txch = config.Can2num[gv.ChannalMapping[gv.MessageData[num][column_index_from_string('F') - 1]]]
	tmplist[ Txch- 1] = '8'
	if config.ExecuteParameter == True:
		if sys.argv[1] == "Clone" and gv.MessageData[num][column_index_from_string('F') - 1] == sys.argv[2]:
			if tmplist[0] == '0':
				tmpRxCH.insert(0, 1)
			if gv.MessageData[num][column_index_from_string('F') - 1] == gv.ChannalMappingConvert["can1"]:
				tmplist[0] = str(int(tmplist[0]) + 8)
			else:
				tmplist[0] = str(int(tmplist[0]) + 1)

	if config.ExecuteParameter == False:
		if config.RunPattern[0] == "Clone" and gv.MessageData[num][column_index_from_string('F') - 1] == config.RunPattern[1]:
			if tmplist[0] == '0':
				tmpRxCH.insert(0, 1)
			if gv.MessageData[num][column_index_from_string('F') - 1] == gv.ChannalMappingConvert["can1"]:
				tmplist[0] = str(int(tmplist[0]) + 8)
			else:
				tmplist[0] = str(int(tmplist[0]) + 1)
	gv.MessageTxCH.append(Txch)
	i = 0
	for tick in gv.MessageData[num][column_index_from_string('L') - 1 : column_index_from_string('G') -2 : -1]:
		if tick.find('√') != -1:
			if config.ExecuteParameter == True:
				if sys.argv[1] == "Clone" and gv.ChannalMappingConvert[config.Num2Can[str(i+1)]] == sys.argv[2]:
					if tmplist[0] == '0':
						tmpRxCH.insert(0, 1)
					if gv.MessageData[num][column_index_from_string('F') - 1] == gv.ChannalMappingConvert["can1"]:
						tmplist[0] = str(int(tmplist[0]) + 8)
					else:
						tmplist[0] = str(int(tmplist[0]) + 1)
			elif config.ExecuteParameter == False:
				if config.RunPattern[0] == "Clone" and gv.ChannalMappingConvert[config.Num2Can[str(i+1)]] == config.RunPattern[1]:
					if tmplist[0] == '0':
						tmpRxCH.insert(0, 1)
					if gv.MessageData[num][column_index_from_string('F') - 1] == gv.ChannalMappingConvert["can1"]:
						tmplist[0] = str(int(tmplist[0]) + 8)
					else:
						tmplist[0] = str(int(tmplist[0]) + 1)
			tmplist[i] = str(int(tmplist[i]) + 1)
			tmpRxCH.append(i + 1)
		i += 1
	gv.MessageRxCH.append(tmpRxCH)
	strtmp += ','.join(tmplist)
	strtmp += "}, "
	return strtmp


#创建报文发送数组
def build_MessageTransmit_Array() -> list:
	MessageTransmit_Array = ["const int MessageTransmit[MessageQuantity][6] = {\n"]
	j = 1
	for i in range(len(gv.MessageData)):
		MessageTransmit_Array.append(__buildTxRxCHArray(i))
		if j % 6 ==0:
			MessageTransmit_Array.append('\n')
		j += 1
	MessageTransmit_Array.append('};\n')
	return MessageTransmit_Array

#创建报文发送数组(克隆)
def build_MessageTransmit_Array_Clone() -> list:
	MessageTransmit_Array = ["const int MessageTransmit[MessageQuantity][6] = {\n"]
	j = 1
	for i in range(len(gv.MessageData)):
		MessageTransmit_Array.append(__buildTxRxCHArrayClone(i))
		if j % 6 ==0:
			MessageTransmit_Array.append('\n')
		j += 1
	MessageTransmit_Array.append('};\n')
	return MessageTransmit_Array


def __buildSignalGenericMessage(num) -> str:
	return "GenericMessage " + 'N' + str(num) + '_' + "Msg_" + gv.MessageData[num][0][2:]  + " = {" + config.MessageTxCH2SpyCH[str(gv.MessageTxCH[num])] + ',' + str(gv.MessageData[num][0]) + ', 0' + ', 0' + ', 8' + '};\n'

#报文结构体定义
def build_GenericMessage() -> list:
	listtmp = []
	for i in range(len(gv.MessageData)):
		listtmp.append(__buildSignalGenericMessage(i))

	return listtmp

#创建定义发送标志位数组
def variable_TxFlag() -> list:
	return ["int TxFlag[MessageQuantity] = {0,};" + '\n']

#创建定义数组ID
def variable_ID() -> list:
	ID = ["char ID[MessageQuantity][6] = \n"]
	j = 1
	st = '{'
	for i in range(len(gv.MessageData)):
		st += '{' + '"'
		st += gv.MessageData[i][column_index_from_string('A') - 1].rstrip(' ')
		st += '"' + '}'
		st += ','
		#print(j)
		if j % 10 == 0:
			st += '\n'
		j += 1
	st += "};\n"
	ID.append(st)

	return ID


#创建定义报文发送时间数组
def variable_MessageSendTime() -> list:
	return "__int64 MessageSendTime[MessageQuantity] = { 0, };\n"

#创建定义报文延时时间变量
def variable_MessageTime() -> list:
	return "__int64 MessageTime[MessageQuantity] = { 0, };\n"

#创建定义报文接收标志数组
def variable_MessageReceive() -> list:
	return "int MessageReceive[MessageQuantity][6] = { 0, };\n"

#创建定义报文发送标志数组
def variable_MessageTransmit() -> list:
	if config.ExecuteParameter == True:
		if sys.argv[1] == "Clone":
			return build_MessageTransmit_Array_Clone()
		else:
			return build_MessageTransmit_Array()
	elif config.ExecuteParameter == False:
		if config.RunPattern[0] == "Clone":
			return build_MessageTransmit_Array_Clone()
		else:
			return build_MessageTransmit_Array()





