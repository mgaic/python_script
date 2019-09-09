from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import random

# cap = {
# 	"platformName": "Android",
# 	"platformVersion": "5.1.1",
# 	"deviceName": "127.0.0.1:62025",
# 	"appPackage": "com.zhuanyejun.club",
# 	"appActivity": "com.zhuanyejun.club.activity.SplashActivity"
# }
cap = {
  "platformName": "Android",
  # "platformVersion": "8.0.0",
  "platformVersion": "5.1.1",
  # "deviceName": "MKJ4C18802001823",

  "deviceName": "127.0.0.1:62025",
  # "deviceName": "192.168.43.4:6666",

  "appPackage": "com.zhuanyejun.club",
  "appActivity": "com.zhuanyejun.club.activity.SplashActivity",
  # "noReset": True
}

def skip_guide():
    x1 = int(width * 0.9)
    y1 = int(height * 0.5)
    x2 = int(width * 0.1)
    time.sleep(1)
    driver.swipe(x1, y1, x2, y1, 2000)
    time.sleep(1)
    driver.swipe(x1, y1, x2, y1, 2000)

def key_board_press(phone_number):
    key_code_table = {
    '0':7,'1':8,'2':9,'3':10,'4':11,'5':12,'6':13,'7':14,'8':15,'9':16,
    'a':29,'b':30,'c':31,'d':32,'e':33,'f':34,'g':35,'h':36,'i':37,'j':38,
    'k':39,'l':40,'m':41,'n':42,'o':43,'p':44,'q':45,'r':46,'s':47,'t':48,
    'u':49,'v':50,'w':51,'x':52,'y':53,'z':54
    }
    for num in phone_number:
        driver.keyevent(key_code_table[num])
        time.sleep(random.uniform(0.5, 1))





driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print("屏幕宽为 " + str(width))
print("屏幕高为 " + str(height))

time.sleep(10)

print("start")
skip_guide()
print("complete")

try:
	enterApp = driver.find_element_by_id("com.zhuanyejun.club:id/introduce_into")
	print("定位到元素,即将点击跳过引导页面")
	enterApp.click()
except Exception as e:
    print("跳过引导页面失败")
    print(e)
    pass


#点击同意 真机会有这一步骤,模拟器中不会
# try:
#     tips_agree_btn = WebDriverWait(driver, 10).until(lambda x : x.find_element_by_xpath("//android.widget.Button[@resource-id='com.zhuanyejun.club:id/positiveButton']"))
#     print("exe here")
#     tips_agree_btn.click()
# except Exception as e:
#     print("tips_agree_btn Exception 已经跳过同意页面")
#     print(e)
#     pass

#点击获取红包
try:
    red_bag_btn = WebDriverWait(driver, 10).until(lambda x : x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.zhuanyejun.club:id/tv_fist_head_red']"))
    print("点击获取红包")
    red_bag_btn.click()
except Exception as e:
    print("red_bag_btn Exception ")
    print(e)
    pass

#点击打开红包按钮
try:
    click_open_red_bag = WebDriverWait(driver, 10).until(lambda x : x.find_element_by_xpath("//android.widget.Image[@text='点击拆红包']"))
    click_open_red_bag.click()
    print("点击拆开红包")
    time.sleep(5)
    
except Exception as e:
    print("click_open_red_bag Exception")
    print(e)
    pass

print("请登录...")


#输入用户名
time.sleep(2)
driver.tap([(370, 280)])
key_board_press("15872998154")



#输入密码
time.sleep(2)
driver.tap([(370, 360)])
key_board_press("qwer66668888")


 
#点击登录按钮
time.sleep(2)
driver.tap([(370, 455)])

#end
print("=="*10 + 'end')