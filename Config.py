import time

OPERATION_DELAY = 0.15 # 操作延时

ADD_POS = (1392, 473) # 默认加价键位置
SUBMIT_POS = (1389, 586) # 默认确认键位置
BID_POS = (1389, 586) # 默认出价键位置
INPUT_POS = (1292, 631) # 默认输入验证码区域


SUBMIT_TIME = "2023-4-9 16:34:49"
SUBMIT_TIMESTAMP = int(time.mktime(time.strptime(SUBMIT_TIME, "%Y-%m-%d %H:%M:%S")))
print(SUBMIT_TIMESTAMP-time.time())

'''
按下 *A* 确认当前鼠标位置为 *加价* 坐标：
(1426, 500)
按下 *S* 确认当前鼠标位置为 *出价* 坐标：
(1426, 624)
按下 *i* 确认当前鼠标位置为 *输入验证码区域* 坐标：
(1347, 675)
按下 *Enter* 确认当前鼠标位置为 *确认* 坐标：
(1160, 773)
Press *A* to bid the price!
Press *Enter* to submit the price!
Please check the *出价* postion!
 *出价* 坐标为 (1426, 624)
Please check the *确认* postion!
 *确认* 坐标为 (1160, 773)

'''
