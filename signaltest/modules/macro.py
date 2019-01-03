import platform
from signaltest.config import g_var

#通道宏定义
macroDefine = ("#define HS_CAN  1\n", "#define MS_CAN  2\n", "#define HS_CAN2 10\n", "#define HS_CAN3 11\n", "#define HS_CAN4 20\n", "#define HS_CAN5 21\n")

#创建测试log宏路径名
def build_testdatapathnamemacrolist(pathname) -> list:
	testdatapathnamemacrolist = []
	if platform.system() == "Linux":
		pathlist = pathname.split('/')
		#print(pathlist)
		datapathname = pathlist[2] + r':\\'
		for dir in pathlist[3:-1]:
			datapathname += dir + r"\\"
		datapathname += "TestData.txt"
		#print(datapathname)
	elif platform.system() == "Windows":
		pathlist = pathname.split('/')
		#print(pathlist)
		datapathname = pathlist[0] + r'\\'
		for dir in pathlist[1:-1]:
			datapathname += dir + r"\\"
		datapathname += "TestData.txt"
		#print(datapathname)

	testdatapathnamemacrolist = ["#define DATAPATHNAME " + '"' + datapathname + '"' + '\n']

	return testdatapathnamemacrolist


#创建报文数量宏定义
def build_msgqtychmacrolist() -> list:
	msgqtychmacrolist = []

	msgqtychmacrolist = ["#define Num_Signal " + str(g_var.Num_Signal) + '\n']

	return msgqtychmacrolist




