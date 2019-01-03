import sys
import os
import platform

import pandas

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl import Workbook
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename
import msgtest
from msgtest.report.testreport import *
from msgtest.modules.readExcel import *
from msgtest.modules.writefile import *
# from msgtest.config.config import *
from msgtest.config import config
from msgtest.config import gv


#生成SpyCCode.c函数
def SpyCCodemain_pandas(pathname):
	gv.MessageQuantity = 0
	gv.MessageData = []
	gv.ChannalMapping = {}
	gv.ChannalMappingConvert = {}
	gv.SpyCCodeTemplateDict = {}  # 定义一个字典用于存储读取的SpyCCode.c模板的数据
	gv.MessageTxCH = []
	gv.MessageRxCH = []
	#调用选择文件夹窗口
	# pathname = askopenfilename(filetypes = [("Excel",".xlsx")])
	if pathname != '':
		# 读取指定列有效数据
		dataFrame = pandas.read_excel(pathname, sheet_name="Sheet1", header=None, na_values="", usecols="A:L")
		# print(dataFrame)
		gv.MessageData = dataFrame.fillna("None").values[2:].tolist()
		# print(gv.MessageData)
		# 将指定列中的None转为NA（为了重用之前版本的代码打个补丁）
		column_None2NA(gv.MessageData, 'C')
		# print(gv.MessageData)

		# 读取指定列数据
		dataFrame = pandas.read_excel(pathname, sheet_name="Sheet1", header=None, na_values="", usecols="M:N")
		# print(dataFrame)
		# 获取通道映射
		gv.ChannalMapping = getChannalMapping_pandas(dataFrame, 0)
		# print(gv.ChannalMapping)
		gv.ChannalMappingConvert = getChannalMapping_pandas(dataFrame, 1)
		# print(gv.ChannalMappingConvert)

		# 创建SpyCCode.c文件
		createSpyCCode(pathname)

		# print(gv.MessageRxCH)

		print('-'*20 + 'END' + '-'*20)

	else:
		print("没有选择路由表")
		exit()

#生成测试报告函数
def reportmain_pandas(routertable_pathname, log_pathname):
	gv.MessageQuantity = 0
	gv.MessageData = []
	gv.ChannalMapping = {}
	gv.ChannalMappingConvert = {}
	gv.SpyCCodeTemplateDict = {}  # 定义一个字典用于存储读取的SpyCCode.c模板的数据
	gv.MessageTxCH = []
	gv.MessageRxCH = []
	#获取测试log数据路径名
	# pathname = askopenfilename(filetypes = [("TXT", ".txt")])
	pathname = log_pathname
	if pathname != '':
		#获取路由表路径名
		# RouterTablepathname = askopenfilename(filetypes = [("Excel", ".xlsx")])
		RouterTablepathname = routertable_pathname
		if RouterTablepathname != '':
			# 读取所有的有效数据
			dataFrame = pandas.read_excel(RouterTablepathname, sheet_name="Sheet1", header=None, na_values="", usecols="A:L")
			# print(dataFrame)
			gv.MessageData = dataFrame.fillna("None").values[2:].tolist()
			# 将指定列中的None转为NA（为了重用之前的代码打个补丁）
			column_None2NA(gv.MessageData, 'C')
			# print(gv.MessageData)

			#设置表名
			SheetTitle = "MessageRouteTestReport"
			#获取测试报告表头列表
			TableHeaderList = build_TableHeaderList_pandas(dataFrame.fillna("None").values[0:2].tolist())
			# print(TableHeaderList)
			#读取SpyCCode生成的log日志
			DataList = readtestlog(pathname)
			#创建测试报告列表
			TestReportList = createmsgtestreportlist(TableHeaderList, DataList)
			#print(testreportlist)
			#设置保存生成报告的路径
			PathName = RouterTablepathname[:pathname.rfind('/')+1] + 'MessageRouteReport.xlsx'
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
