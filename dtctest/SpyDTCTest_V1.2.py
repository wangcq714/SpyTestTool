import sys
import os
import platform

import pandas

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl import Workbook
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename

from config.config import *
from config import global_var
from modules.readExcel import *
from modules.writefile import *
from report.testreport import *


#生成SpyCCode.c函数
def SpyCCodemain():
	#调用选择文件夹窗口
	pathname = askopenfilename(filetypes = [("Excel",".xlsx")])
	if pathname != ():
		# 读取指定列的数据
		dataFrame = pandas.read_excel(pathname, sheet_name="DTC", header=None, na_values="", usecols="A:J")
		# print(dataFrame)
		# 将Frame格式数据转换成列表
		global_var.DTC_Datas = dataFrame.fillna("None").values[2:].tolist()
		# print(global_var.DTC_Datas)
		# 对读取到的列表数据进行处理，获得节点丢失DTC数据行,并将所有int元素转为str类型
		global_var.DTC_Datas = DTC_Datas_handling(global_var.DTC_Datas)
		# print(global_var.DTC_Datas)
		global_var.Num_DTC = len(global_var.DTC_Datas)
		# print(global_var.Num_DTC)

		# 获取通道映射
		# 读取指定列数据
		dataFrame = pandas.read_excel(pathname, sheet_name="DTC", header=None, na_values="", usecols="M:N")
		# print(dataFrame)
		# 获取通道映射
		global_var.ChannalMapping = getChannalMapping_pandas(dataFrame, 0)
		# print(global_var.ChannalMapping)
		global_var.ChannalMappingConvert = getChannalMapping_pandas(dataFrame, 1)
		# print(global_var.ChannalMappingConvert)

		# 读取诊断ID配置信息
		DiagCH, global_var.Diag_Req_ID, global_var.Diag_Res_ID = get_para_set_pandas(dataFrame)
		global_var.DiagCH = MessageTxCH2SpyCH[str(Can2num[global_var.ChannalMapping[DiagCH].lower()])]
		# print(global_var.DiagCH)
		# print(global_var.Diag_Req_ID)
		# print(global_var.Diag_Res_ID)

		# 创建SpyCCode.c文件
		createSpyCCode(pathname)


		print('-'*20 + 'END' + '-'*20)

	else:
		print("没有选择路由表")
		exit()

#生成测试报告函数
def reportmain():
	#获取测试log数据路径名
	pathname = askopenfilename(filetypes = [("TXT",".txt")])
	if pathname != ():
		#获取路由表路径名
		RouterTablepathname = askopenfilename(filetypes = [("Excel",".xlsx")])
		if RouterTablepathname != '':
			# 读取指定列的数据
			dataFrame = pandas.read_excel(RouterTablepathname, sheet_name="DTC", header=None, na_values="", usecols="A:J")
			# print(dataFrame)
			# 将Frame格式数据转换成列表
			global_var.DTC_Datas = dataFrame.fillna("None").values[2:].tolist()
			# print(global_var.DTC_Datas)

			#设置表名
			SheetTitle = "MessageRouteTestReport"			
			#获取测试报告表头列表
			TableHeaderList = build_TableHeaderList(dataFrame.fillna("None").values[0:2].tolist())
			# print(TableHeaderList)
			#读取SpyCCode生成的log日志
			DataList = readtestlog(pathname)
			# print(DataList)
			# print(len(DataList))
			#创建测试报告列表
			TestReportList = createmsgtestreportlist(TableHeaderList, DataList)
			# print(TestReportList)
			#设置保存生成报告的路径
			PathName = RouterTablepathname[:pathname.rfind('/')+1] + 'DTCReport.xlsx'
			#将测试报告数据写入excel
			write2excel(SheetTitle, TestReportList, PathName) 
			#设置测试报告Excel表格式
			setstyle(PathName, SheetTitle)

			#结束行
			print('-'*20 + "END" + '-'*20)

		else:
			print("没有选择路由表")
			exit()
	else:
		print("没有选择data.txt文件")
		exit()

def main():
	#判断生成文件类型  1."Test"
	if ExecuteParameter == True:
		try:
			runPattern = sys.argv[1]
		except (IndexError, ):
			print("请给程序传参：python3 文件名.py Test or python3 文件名.py Report")
			exit()
			
		if sys.argv[1] == "Test":
			SpyCCodemain()
		elif sys.argv[1] == "Report":
			reportmain()
		else:
			print("RunPattern setup error!!!")
			exit()

	elif ExecuteParameter == False:
		if RunPattern[0] == "Test":
			SpyCCodemain()
		elif RunPattern[0] == "Report":
			reportmain()
		else:
			print("RunPattern setup error!!!")
			exit()



if __name__ == '__main__':
	main()