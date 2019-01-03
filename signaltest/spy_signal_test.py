import sys
import os
import platform

import pandas

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl import Workbook
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename

from signaltest.report.testreport import *
from signaltest.modules.readExcel import *
from signaltest.modules.writefile import *
from signaltest.config.config import *
from signaltest.config import g_var



#生成SpyCCode.c函数
def SpyCCodemain_pandas(pathname):
	g_var.Num_Signal = 0
	g_var.SignalDatas = []
	g_var.ChannalMapping = {}
	g_var.ChannalMappingConvert = {}
	g_var.SpyCCodeTemplateDict = {}  # 定义一个字典用于存储读取的SpyCCode.c模板的数据
	g_var.MessageTxCH = []
	g_var.MessageRxCH = []
	#调用选择文件夹窗口
	# pathname = askopenfilename(filetypes = [("Excel",".xlsx")])
	if pathname != '':
		# 读取指定列有效数据
		dataFrame = pandas.read_excel(pathname, sheet_name="Sheet2", header=None, na_values="", usecols="A:T")
		# print(dataFrame)
		# 将DataFrame格式数据转为列表
		g_var.SignalDatas = dataFrame.fillna("None").values[2:].tolist()
		# print(g_var.SignalDatas)
		# 将列表中的所有int转为str
		g_var.SignalDatas = SignalDatas_handling(g_var.SignalDatas)
		# print(g_var.SignalDatas)
		g_var.Num_Signal = len(g_var.SignalDatas)
		# print(g_var.Num_Signal)

		# 读取指定列数据
		dataFrame = pandas.read_excel(pathname, sheet_name="Sheet2", header=None, na_values="", usecols="V:X")
		# print(dataFrame)
		# 获取通道映射
		g_var.ChannalMapping = getChannalMapping_pandas(dataFrame, 0)
		# print(g_var.ChannalMapping)
		g_var.ChannalMappingConvert = getChannalMapping_pandas(dataFrame, 1)
		# print(g_var.ChannalMappingConvert)

		# 创建SpyCCode.c文件
		createSpyCCode(pathname)


		print('-'*20 + 'END' + '-'*20)

	else:
		print("没有选择路由表")
		exit()


#生成测试报告函数
def reportmain_pandas(pathname, SignalTablepathname):
	g_var.Num_Signal = 0
	g_var.SignalDatas = []
	g_var.ChannalMapping = {}
	g_var.ChannalMappingConvert = {}
	g_var.SpyCCodeTemplateDict = {}  # 定义一个字典用于存储读取的SpyCCode.c模板的数据
	g_var.MessageTxCH = []
	g_var.MessageRxCH = []
	#获取测试log数据路径名
	# pathname = askopenfilename(filetypes = [("TXT",".txt")])
	if pathname != '':
		#获取路由表路径名
		# SignalTablepathname = askopenfilename(filetypes = [("Excel",".xlsx")])
		if SignalTablepathname != '':
			# 读取指定列有效数据
			dataFrame = pandas.read_excel(SignalTablepathname, sheet_name="Sheet2", header=None, na_values="", usecols="A:T")
			# print(dataFrame)
			# 将DataFrame格式数据转为列表
			g_var.SignalDatas = dataFrame.fillna("None").values[2:].tolist()
			# print(g_var.SignalDatas)
			# 将列表中的所有int转为str
			g_var.SignalDatas = SignalDatas_handling(g_var.SignalDatas)
			# print(g_var.SignalDatas)
			g_var.Num_Signal = len(g_var.SignalDatas)
			# print(g_var.Num_Signal)



			#设置表名
			SheetTitle = "SignalTestReport"			
			#获取测试报告表头列表
			TableHeaderList = build_TableHeaderList_pandas(dataFrame.fillna("None").values[0:2].tolist())
			#print(TableHeaderList)
			#读取SpyCCode生成的log日志
			DataList = readtestlog(pathname)
			#print(DataList)
			#创建测试报告列表
			TestReportList = create_Signal_testreportlist(TableHeaderList, DataList)
			#print(TestReportList)
			#设置保存生成报告的路径
			PathName = SignalTablepathname[:pathname.rfind('/')+1] + 'SignalTestReport.xlsx'
			#将测试报告数据写入excel
			write2excel(SheetTitle, TestReportList, PathName) 
			#设置测试报告Excel表格式
			setstyle(PathName, SheetTitle)

			#结束行
			print('-'*20 + "END" + '-'*20)

		else:
			print("没有选择路由表")
	else:
		print("没有选择data.txt文件")
		exit()


