'''
运行模式：
		Test: 默认模式
		Report： 生成测试报告
'''

RunPattern = ["Test"]
#RunPattern = ["Report"]

#设置程序是否以传参模式运行
# ExecuteParameter = True
ExecuteParameter = False

DiagCH = "HS_CAN"
Diag_Req_ID = "0x76F"
Diag_Res_ID = "0x70F"








#can通道与数字映射
Can2num = {"can1":1, "can2":2, "can3":3, "can4":4, "can5":5, "can6":6}

#数字与can通道映射
Num2Can = {'1':"can1", '2':"can2", '3':"can3", '4':"can4", '5':"can5", '6':"can6"}

#报文发送can通道与Spy通道映射
MessageTxCH2SpyCH = {'1':"HS_CAN", '2':"HS_CAN2", '3':"HS_CAN3", '4':"HS_CAN4", '5':"HS_CAN5", '6':"MS_CAN"}










