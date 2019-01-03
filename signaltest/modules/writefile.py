# from signaltest.config import g_var
# from signaltest.config.config import *
from signaltest.modules.buildfun import *
from signaltest.modules.buildVariable import *
from signaltest.modules.SpyCCodeTemplateData import *
from signaltest.modules.macro import *

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

	write2Cfile(Cfile, build_Dest_Signal_Type_struct())
	writenullline(Cfile)
	write2Cfile(Cfile, build_Test_Num_var())
	writenullline(Cfile)
	write2Cfile(Cfile, build_Source_SignalPeriod_Array())
	writenullline(Cfile)
	write2Cfile(Cfile, build_DestSignal_Array())
	writenullline(Cfile)
	write2Cfile(Cfile, build_DestSignalMask_Array())
	writenullline(Cfile)
	write2Cfile(Cfile, build_SourceSignal_Value0_Array())
	writenullline(Cfile)
	write2Cfile(Cfile, build_SourceSignal_Value1_Array())
	writenullline(Cfile)
	write2Cfile(Cfile, build_TestEnable_Array())
	writenullline(Cfile)
	write2Cfile(Cfile, build_TestFlag_Array())
	writenullline(Cfile)
	write2Cfile(Cfile, build_LoopCount_Array())
	writenullline(Cfile)
	writenullline(Cfile)

	write2Cfile(Cfile, build_SpyRxDestSignal_func())
	writenullline(Cfile)
	write2Cfile(Cfile, build_SpyRxSignal_func())
	writenullline(Cfile)
	write2Cfile(Cfile, build_Spy_EveryMessage_func())
	writenullline(Cfile)
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_EveryLongMessage"])
	writenullline(Cfile)
	write2Cfile(Cfile, build_SpyTxSignal_func())
	writenullline(Cfile)
	write2Cfile(Cfile, build_Spy_EveryLoop_func())
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
	write2Cfile(Cfile, build_printlog_func())
	writenullline(Cfile)
	write2Cfile(Cfile, build_write2txt_func())
	writenullline(Cfile)
	write2Cfile(Cfile, build_Spy_Signal_Test_func())
	writenullline(Cfile)
	write2Cfile(Cfile, build_Spy_Main_func())
	writenullline(Cfile)

	Cfile.close()


