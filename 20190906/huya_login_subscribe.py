
from selenium import webdriver
# from selenium.webdriver.chrome.options import Chrome
import time
from urllib.parse import quote
import traceback


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#配置Chrome参数

option = webdriver.ChromeOptions()
# option.add_argument("--start-maximized")

# option.add_extension(proxy_auth_plugin_path)

driver = webdriver.Chrome('D:\\Google\\Chrome\\Application\\chromedriver.exe', options=chromeOptions)

#待访问的URL
url = 'https://www.huya.com/16476414'

#窗口最大化
driver.maximize_window()
driver.delete_all_cookies()

#发起请求
driver.get(url)

time.sleep(3) #让页面加载一会儿

#显示等待10s，直到出现登录按钮并点击该按钮，否则抛异常
try: 
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-login'))
    )
    login_button.click()
    print("点击登录成功")
except:
    driver.quit()
    exit()

#踩坑处 记得要切换到登录frame 否则无法定位到登录框中的元素
driver.switch_to_frame("UDBSdkLgn_iframe")

#切换到手机号码登录，默认是账号登录
element = driver.find_element_by_xpath('//*[@id="login-head-nav"]/ul/li[2]')
element.click()


try:
	#定位到手机号输入框，并输入手机号
    number_input = WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH, '//*[@id="phone-login-form"]/div[1]/input'))
    )   
    print("定位到number元素")
    phone_number = input("请输入手机号")
    number_input.send_keys(phone_number)
    print("发送成功")

    #定位并点击获取手机验证码按钮
    get_code_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="phone-login-form"]/div[2]/span'))
    )
    get_code_button.click()
    print("点击获取验证码成功")

    code = input("请输入验证码")

    #定位到验证码输入框
    code_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="phone-login-form"]/div[2]/input'))
    )

    #输入验证码
    code_input.send_keys(code)
    
    #定位到登录按钮并登录
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="phone-login-btn"]'))
    )
    login_button.click()
    print("登录成功")

except:
    print(e)

#从frame切回主文档，至关重要
# driver.switch_to.default_content()
driver.refresh()  #刷新页面

#定位到订阅按钮，如何显示的是订阅，则点击订阅，如果已经订阅，则退出
try: 
    his_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="yyliveRk_game_newsBut"]/div[1]'))
    )
    his_button.click()
    print("订阅成功")
except Exception as e:
    print(e)
