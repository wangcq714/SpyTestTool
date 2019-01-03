import os
# from dtctest.config.config import *
from dtctest.config import global_var
# from dtctest.config import *
#from dtctest.modules.buildfun import *
from dtctest.modules.buildVariable import *
from dtctest.modules.SpyCCodeTemplateData import *
from dtctest.modules.macro import *
from dtctest.modules.SpyCCodeTemplateData import *
from dtctest.modules.buildfun import *

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
	#os.mkdir(pathname[:pathname.rfind('/')+1] + "./DTC")
	Cfile = open(pathname[:pathname.rfind('/')+1] + "/SpyCCode.c", 'w')

	#写入头文件
	write2Cfile(Cfile, SpyCCodeTemplateDict["headerfile"])
	writenullline(Cfile)

	#写入Spy通道映射宏定义
	write2Cfile(Cfile, Spy_Ch_Define_macro)
	writenullline(Cfile)

	#写入DTC数量宏定义
	write2Cfile(Cfile, build_Num_DTC_macro(global_var.Num_DTC))
	writenullline(Cfile)

	#写入诊断通道映射宏定义
	write2Cfile(Cfile, build_DiagCH_macro(global_var.DiagCH))
	writenullline(Cfile)

	#写入诊断请求ID宏定义
	write2Cfile(Cfile, build_Diag_Req_ID_macro(global_var.Diag_Req_ID))
	writenullline(Cfile)

	#写入诊断响应ID宏定义
	write2Cfile(Cfile, build_Diag_Res_ID_macro(global_var.Diag_Res_ID))
	writenullline(Cfile)

	#写入保存测试数据路径宏定义
	write2Cfile(Cfile, build_testlog_pathname_macro(pathname))
	writenullline(Cfile)

	#写入DTC数组定义
	write2Cfile(Cfile, build_DTC_array())
	#写入报文周期数组定义
	write2Cfile(Cfile, build_MsgPeriod_array())
	writenullline(Cfile)

	#写入ReportDTCCycle定义
	write2Cfile(Cfile, build_ReportDTCCycle())
	#写入ReportDTCTimer数组定义
	write2Cfile(Cfile, build_ReportDTCTimer_array())
	#写入ClearDTCTimer
	write2Cfile(Cfile, build_ClearDTCTimer())
	writenullline(Cfile)

	#写入Msg测试使能数组
	write2Cfile(Cfile, build_MsgTestEnable_array())
	#写入Msg发送使能数组
	write2Cfile(Cfile, build_MsgTxEnable_array())
	writenullline(Cfile)

	#写入Msg发送标志数组
	write2Cfile(Cfile, build_MsgTxFlag_array())
	writenullline(Cfile)

	#写入诊断请求10 03标志数组
	write2Cfile(Cfile, build_DiagReqFlag_1003_array())
	#写入诊断响应10 03标志数组
	write2Cfile(Cfile, build_DiagResFlag_1003_array())
	writenullline(Cfile)

	#写入诊断请求14 FF FF FF标志数组
	write2Cfile(Cfile, build_DiagReqFlag_14_array())
	#写入诊断响应14 FF FF FF标志数组
	write2Cfile(Cfile, build_DiagResFlag_14_array())
	writenullline(Cfile)

	#写入诊断请求19 04 xx xx xx 2F标志数组
	write2Cfile(Cfile, build_DiagReqFlag_1904_array())
	#写入诊断响应59 04 xx xx xx 00标志数组
	write2Cfile(Cfile, build_DiagResFlag_1904_00_array())
	#写入诊断响应59 04 xx xx xx 2E标志数组
	write2Cfile(Cfile, build_DiagResFlag_1904_2E_array())
	#写入诊断响应59 04 xx xx xx 2F标志数组
	write2Cfile(Cfile, build_DiagResFlag_1904_2F_array())
	writenullline(Cfile)

	#写入周期函数循环计数数组定义
	write2Cfile(Cfile, build_LoopCount_array())
	writenullline(Cfile)

	#写入Msg_76F_10_03数组定义
	write2Cfile(Cfile, build_Msg_76F_10_03())
	writenullline(Cfile)

	#写入Msg_76F_14数组定义
	write2Cfile(Cfile, build_Msg_76F_14())
	writenullline(Cfile)

	#写入build_Msg_76F_19_04数组定义
	write2Cfile(Cfile, build_Msg_76F_19_04_array())
	writenullline(Cfile)

	#写入Msg数组定义
	write2Cfile(Cfile, build_Msg_array())
	writenullline(Cfile)

	#写入Spy_Diag_Req_Msg函数定义
	write2Cfile(Cfile, build_Spy_Diag_Req_Msg_func())
	writenullline(Cfile)

	#写入Spy_Diag_Res_Msg函数定义
	write2Cfile(Cfile, build_Spy_Diag_Res_Msg_func())
	writenullline(Cfile)

	#写入Spy_TxRxMsg_Flag函数定义
	write2Cfile(Cfile, build_Spy_TxRxMsg_Flag_func())
	writenullline(Cfile)

	#写入Spy_EveryMessage函数定义
	write2Cfile(Cfile, build_Spy_EveryMessage_func())
	writenullline(Cfile)

	#写入Spy_EveryLongMessage函数定义
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_EveryLongMessage"])
	writenullline(Cfile)

	#写入Spy_TxMsg函数定义
	write2Cfile(Cfile, build_Spy_TxMsg_func())
	writenullline(Cfile)

	#写入Spy_EveryLoop函数定义
	write2Cfile(Cfile, build_Spy_EveryLoop_func())
	writenullline(Cfile)

	#写入Spy_EveryGUILoop函数定义
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_EveryGUILoop"])
	writenullline(Cfile)

	#写入Spy_ErrorState函数定义
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_ErrorState"])
	writenullline(Cfile)

	#写入Spy_ErrorFrame函数定义
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_ErrorFrame"])
	writenullline(Cfile)

	#写入Spy_Stopped函数定义
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_Stopped"])
	writenullline(Cfile)

	#写入Spy_KeyPress函数定义
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_KeyPress"])
	writenullline(Cfile)

	#写入SSpy_Started函数定义
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_Started"])
	writenullline(Cfile)

	#写入Spy_BeforeStarted函数定义
	write2Cfile(Cfile, SpyCCodeTemplateDict["Fun_Spy_BeforeStarted"])
	writenullline(Cfile)

	#写入build_printlog_func函数定义
	write2Cfile(Cfile, build_printlog_func())
	writenullline(Cfile)

	#写入build_write2txt_func函数定义
	write2Cfile(Cfile, build_write2txt_func())
	writenullline(Cfile)

	#写入build_Spy_DTC_Test_func函数定义
	write2Cfile(Cfile, build_Spy_DTC_Test_func())
	writenullline(Cfile)

	#写入build_Spy_Main_func函数定义
	write2Cfile(Cfile, build_Spy_Main_func())
	writenullline(Cfile)


	Cfile.close()


