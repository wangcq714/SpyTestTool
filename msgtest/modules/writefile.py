from msgtest.config import gv
# from msgtest.config.config import *
# from msgtest.config import config
from msgtest.modules.buildfun import *
from msgtest.modules.buildVariable import *
from msgtest.modules.SpyCCodeTemplateData import *
from msgtest.modules.macro import *

#按行写入.C文件
def write2Cfile(Cfile, content:list) -> None:
	for tmp in content:
		Cfile.write(tmp)

#插入一个空行
def writenullline(Cfile) -> None:
	Cfile.write('\n')


#写入SpyCCode.c文件
def createSpyCCode(pathname) -> None:
	#创建一个指定路径下的.C文件，如已存在则覆盖
	Cfile = open(pathname[:pathname.rfind('/')+1] + "SpyCCode.c", 'w')

	#写入头文件
	write2Cfile(Cfile, SpyCCodeTemplateDict["headerfile"])
	writenullline(Cfile)

	#写入宏定义
	write2Cfile(Cfile, macroDefine)
	writenullline(Cfile)
	#写入报文数量宏定义
	write2Cfile(Cfile, build_msgqtychmacrolist())
	writenullline(Cfile)
	#写入保存测试数据路径宏定义
	write2Cfile(Cfile, build_testdatapathnamemacrolist(pathname))
	writenullline(Cfile)

	#写入发送标志位数组
	write2Cfile(Cfile, variable_TxFlag())
	writenullline(Cfile)
	#写入ID数组
	write2Cfile(Cfile, variable_ID())
	#写入报文发送时间数组
	write2Cfile(Cfile, variable_MessageSendTime())
	#写入报文延时时间数组
	write2Cfile(Cfile, variable_MessageTime())
	#写入接收报文数组
	write2Cfile(Cfile, variable_MessageReceive())
	#写入报文发送数组
	write2Cfile(Cfile, variable_MessageTransmit())
	writenullline(Cfile)
	#写入报文定义数组
	write2Cfile(Cfile, build_GenericMessage())
	writenullline(Cfile)

	#写入函数定义
	write2Cfile(Cfile, build_build_SpyTxRxMsgFun())
	writenullline(Cfile)
	write2Cfile(Cfile, build_Spy_EveryMessageFun())
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_EveryLongMessage"])
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_EveryLoop"])
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_EveryGUILoop"])
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_ErrorState"])
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_ErrorFrame"])
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_Stopped"])
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_KeyPress"])
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_Started"])
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_BeforeStarted"])
	writenullline(Cfile)
	write2Cfile(Cfile, build_printlogFun())
	writenullline(Cfile)
	write2Cfile(Cfile, build_debugfun())
	writenullline(Cfile)
	write2Cfile(Cfile, build_write2txtfun())
	writenullline(Cfile)
	write2Cfile(Cfile, build_Spy_Main())
	writenullline(Cfile)

	Cfile.close()


