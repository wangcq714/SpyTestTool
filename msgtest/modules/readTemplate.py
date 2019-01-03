from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename

#读取SpyCCode.c文件中空模板数据,将每个函数存储在相应字典中，返回字典
def readSpyCCodeTemplate(pathname:str) -> dict:
	SpyCCodeTemplateDict = {}
	TemplateData = []

	#读取模板中所有行保存在临时列表TemplateData中
	with open(pathname) as file:
		for line in file:
			TemplateData.append(line)

	#切片获得headerfile
	SpyCCodeTemplateDict["headerfile"] = []
	for tmp in TemplateData[0:9]:	
		SpyCCodeTemplateDict["headerfile"].append(tmp)

	#切片获得Fun_Spy_EveryMessage
	SpyCCodeTemplateDict["Fun_Spy_EveryMessage"] = []
	for tmp in TemplateData[9:17]:		
		SpyCCodeTemplateDict["Fun_Spy_EveryMessage"].append(tmp)

	#切片获得Fun_Spy_EveryLongMessage
	SpyCCodeTemplateDict["Fun_Spy_EveryLongMessage"] = []
	for tmp in TemplateData[17:22]:
		SpyCCodeTemplateDict["Fun_Spy_EveryLongMessage"].append(tmp)

	#切片获得Fun_Spy_EveryLoop
	SpyCCodeTemplateDict["Fun_Spy_EveryLoop"] = []
	for tmp in TemplateData[22:27]:		
		SpyCCodeTemplateDict["Fun_Spy_EveryLoop"].append(tmp)

	#切片获得Fun_Spy_EveryGUILoop
	SpyCCodeTemplateDict["Fun_Spy_EveryGUILoop"] = []
	for tmp in TemplateData[27:32]:	
		SpyCCodeTemplateDict["Fun_Spy_EveryGUILoop"].append(tmp)

	#切片获得Fun_Spy_ErrorState
	SpyCCodeTemplateDict["Fun_Spy_ErrorState"] = []
	for tmp in TemplateData[32:36]:
		SpyCCodeTemplateDict["Fun_Spy_ErrorState"].append(tmp)

	#切片获得Fun_Spy_ErrorFrame
	SpyCCodeTemplateDict["Fun_Spy_ErrorFrame"] = []
	for tmp in TemplateData[36:40]:
		SpyCCodeTemplateDict["Fun_Spy_ErrorFrame"].append(tmp)

	#切片获得Fun_Spy_Stopped
	SpyCCodeTemplateDict["Fun_Spy_Stopped"] = []
	for tmp in TemplateData[40:45]:
		SpyCCodeTemplateDict["Fun_Spy_Stopped"].append(tmp)

	#切片获得Fun_Spy_KeyPress
	SpyCCodeTemplateDict["Fun_Spy_KeyPress"] = []
	for tmp in TemplateData[45:50]:	
		SpyCCodeTemplateDict["Fun_Spy_KeyPress"].append(tmp)

	#切片获得Fun_Spy_Started
	SpyCCodeTemplateDict["Fun_Spy_Started"] = []
	for tmp in TemplateData[50:55]:	
		SpyCCodeTemplateDict["Fun_Spy_Started"].append(tmp)

	#切片获得Fun_Spy_BeforeStarted
	SpyCCodeTemplateDict["Fun_Spy_BeforeStarted"] = []
	for tmp in TemplateData[55:60]:	
		SpyCCodeTemplateDict["Fun_Spy_BeforeStarted"].append(tmp)

	#切片获得Fun_Spy_Main
	SpyCCodeTemplateDict["Fun_Spy_Main"] = []
	for tmp in TemplateData[60:70]:	
		SpyCCodeTemplateDict["Fun_Spy_Main"].append(tmp)

	print(SpyCCodeTemplateDict)
	return SpyCCodeTemplateDict






if __name__ == "__main__":
	pathname = askopenfilename(filetypes = [("C",".c")])
	if pathname != '':
		for k, v in readSpyCCodeTemplate(pathname).items():
			print("%s : %s\n"%(k,v))


