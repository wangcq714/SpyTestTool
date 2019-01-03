#存储SpyCCode.c原始文件数据
SpyCCodeTemplateDict = {}

SpyCCodeTemplateDict["headerfile"] = ('////////////////////////////////////////\n', '// Spy C Code Implementation\n', \
										'////////////////////////////////////////\n', '#include "vspy.h"\n', '// module variables\n', \
										'// TODO: add global variables here\n', '\n', '// TODO: add event handlers here\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_EveryMessage"] = ('void Spy_EveryMessage(GenericMessage * p_Msg)\n', '{\n', '\t// TODO: add something you \
												want to do for every message\n', '\n', '\t//printf("Spy_EveryMessage");\n', '\n', '}\n', '\n')

SpyCCodeTemplateDict["Fun_Spy_EveryLongMessage"] = ('void Spy_EveryLongMessage(GenericLongMessage * p_Msg)\n', '{\n', '\t// TODO: add something you want to do for every long message\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_EveryLoop"] = ('void Spy_EveryLoop(unsigned int uiCurrentTime)\n', '{\n', '\t// TODO: add something you want to do every millisecond\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_EveryGUILoop"] = ('void Spy_EveryGUILoop()\n', '{\n', '\t// TODO: write code to interact with the vehicle spy gui (this is called on the GUI thread)\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_ErrorState"] = ('void Spy_ErrorState(int iNetwork, int iTxErrorCount, int iRxErrorCount, int iErrorBitfield)\n', '{\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_ErrorFrame"] = ('void Spy_ErrorFrame(int iNetwork, int iTxErrorCount, int iRxErrorCount, int iErrorBitfield)\n', '{\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_Stopped"] = ('void Spy_Stopped()\n', '{\n', '\t// TODO: add stopped code\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_KeyPress"] = ('void Spy_KeyPress(int iKey, int iCTRLPressed, int iALTPressed)\n', '{\n', '\t// TODO: add key handler code\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_Started"] = ('void Spy_Started()\n', '{\n', '\t// TODO: add started code\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_BeforeStarted"] = ('void Spy_BeforeStarted()\n', '{\n', '\t// TODO: add before started code\n', '}\n', '\n')


SpyCCodeTemplateDict["Fun_Spy_Main"] = ('void Spy_Main()\n', '{\n', '\t// TODO: Add code here to run every time Spy is run\n', '\tdo \n', \
										'\t{\n', '\t\t// delay for one second\n', '\t\tSleep(100);\t\t\n', '\t} while (1);\n', '}\n')




