import platform

#通道宏定义
Spy_Ch_Define_macro = ("#define HS_CAN  1\n", "#define MS_CAN  2\n", "#define HS_CAN2 10\n", "#define HS_CAN3 11\n", "#define HS_CAN4 20\n", "#define HS_CAN5 21\n")

#创建测试log宏路径名
def build_testlog_pathname_macro(pathname) -> list:
	testdatapathnamemacrolist = []
	if platform.system() == "Linux":
		pathlist = pathname.split('/')
		#print(pathlist)
		datapathname = pathlist[2] + r':\\'
		for dir in pathlist[3:-1]:
			datapathname += dir + r"\\"
		datapathname += "DTCTestData.txt"
		#print(datapathname)
	elif platform.system() == "Windows":
		pathlist = pathname.split('/')
		#print(pathlist)
		datapathname = pathlist[0] + r'\\'
		for dir in pathlist[1:-1]:
			datapathname += dir + r"\\"
		datapathname += "DTCTestData.txt"
		#print(datapathname)

	testdatapathnamemacrolist = ["#define DATAPATHNAME " + '"' + datapathname + '"' + '\n']

	return testdatapathnamemacrolist


#创建报文数量宏定义
def build_Num_DTC_macro(g_Num_DTC) -> list:
	Num_DTC_macrolist = []
	Num_DTC_macrolist = ["#define Num_DTC " + str(g_Num_DTC) + '\n']

	return Num_DTC_macrolist

#创建诊断通道配置宏
def build_DiagCH_macro(DiagCH) -> list:
	DiagCH_macrolist = []
	DiagCH_macrolist = ["#define DiagCH " + DiagCH + '\n']

	return DiagCH_macrolist

#创建诊断请求ID配置宏
def build_Diag_Req_ID_macro(Diag_Req_ID) -> list:
	Diag_Req_ID_macrolist = []
	Diag_Req_ID_macrolist = ["#define Diag_Req_ID " + Diag_Req_ID + '\n']

	return Diag_Req_ID_macrolist


#创建诊断响应ID配置宏
def build_Diag_Res_ID_macro(Diag_Res_ID) -> list:
	Diag_Res_ID_macrolist = []
	Diag_Res_ID_macrolist = ["#define Diag_Res_ID " + Diag_Res_ID + '\n']

	return Diag_Res_ID_macrolist






