import time
import random
from PIL import Image
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from jiema import Chaojiying_Client

EMAIL = 'cqc@cuiqingcai.com'
PASSWORD = 'qwer66668888'
BORDER = 6
INIT_LEFT = 60
CHAOJIYING_USERNAME = '15872998154' #超级鹰账号
CHAOJIYING_PASSWORD = 'qwer66668888' #超级鹰密码
CHAOJIYING_PASSWORD_SOFTWARE_ID = '901519' #超级鹰软件ID，需至平台申请
CODETYPE = 9004

class CrackGeetest():

    def __init__(self):
        self.pic_id = ''
        self.option = webdriver.ChromeOptions()
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome('D:\\Google\\Chrome\\Application\\chromedriver.exe', options = self.option)
        # self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
    
    def __del__(self):
        self.browser.close()
    
    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return:
        """
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="captchaIdLogin"]/div/div[3]')))
        return button
    
    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        try:
            img = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div')))
        except:
            print("未定位到验证码图片")
            exit()
        # time.sleep(1000)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)
    
    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot
    
    # def get_slider(self):
    #     """
    #     获取滑块
    #     :return: 滑块对象
    #     """
    #     slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
    #     return slider
    
    def get_geetest_image_and_position(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom-60))
        captcha.save(name)
        # captcha.show()
        position = (top, bottom, left, right,)
        # time.sleep(1000)
        return captcha, position
    
    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.maximize_window()
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div/div/input')))
        password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[1]/div/input')))
        email.send_keys(self.email)
        password.send_keys(self.password)
    
    
    
    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[5]')))
        submit.click()
        time.sleep(10)
        print('登录成功')

    def submit_captcha_img_get_click_cor(self):
        print("正在提交验证码")
        chaojiying = Chaojiying_Client(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_PASSWORD_SOFTWARE_ID)
        im = open('./captcha1.png', 'rb').read()
        res_str = chaojiying.PostPic(im, CODETYPE)
        if res_str['err_no'] == 0:
            self.pic_id = res_str['pic_id']
            pic_str = res_str['pic_str']
            click_cor = list(map(lambda x:x.split(','),pic_str.split('|')))
            print(click_cor)
            
            return click_cor
        else:
            return list()
    
    def crack(self):
        # 输入用户名密码
        self.open()
        # 点击验证按钮
        button = self.get_geetest_button()
        button.click()
        # 获取验证码图片
        image_info = self.get_geetest_image_and_position('captcha1.png')
        image1 = image_info[0]
        position = image_info[1]
        # image1.show()
        click_cor = self.submit_captcha_img_get_click_cor()
        for each_cor in click_cor:
            self.click_cor(each_cor)
            time.sleep(random.uniform(1, 1.5))  
        self.submit_captcha()
        

        if self.captcha_is_passed():
            print("验证通过")
            self.login()
        else:
            Chaojiying_Client(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_PASSWORD_SOFTWARE_ID).ReportError(self.pic_id)
            # print("验证未通过,请重试")
            time.sleep(random.uniform(3, 4))
            self.input_captcha_again()


        

        # time.sleep(1000)
    
    def input_captcha_again(self):
        image_info = self.get_geetest_image_and_position('captcha1.png')
        # time.sleep(1000)
        image1 = image_info[0]
        position = image_info[1]
        click_cor = self.submit_captcha_img_get_click_cor()
        for each_cor in click_cor:
            self.click_cor(each_cor)
            time.sleep(random.uniform(1, 1.5))  
        self.submit_captcha()
        if self.captcha_is_passed():
            # print("验证通过")
            self.login()
        else:
            Chaojiying_Client(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_PASSWORD_SOFTWARE_ID).ReportError(self.pic_id)
            # print("验证未通过,请重试")
            self.input_captcha_again()

        

    def submit_captcha(self):
        print("提交验证码")
        # ActionChains(self.browser).move_by_offset(position[3]-20, position[1]-20).click().perform()
        submit_captcha_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div[3]/a/div')))
        submit_captcha_btn.click()

        # time.sleep(1000) 

    def click_cor(self, cor):
        # print("左上角坐标{},{}".format( self.get_position()[0], self.get_position()[2]))
        print("返回坐标{},{}".format(int(cor[0]), int(cor[1])))
        
        # cor_x = int(cor[1]) + self.get_position()[0] 
        # cor_y = int(cor[0]) + self.get_position()[2]
        # print("要点击的坐标为{},{}".format(cor_x, cor_y))
        img = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div')
        # ActionChains(driver).move_to_element(ele).move_by_offset(5,5).click().perform()
        ActionChains(self.browser).move_to_element_with_offset(img, int(cor[0]), int(cor[1])).click().perform()
        time.sleep(1)
        print("点击完成")
        # .move_by_offset(20, 100).
        # print("{},{}坐标已经点击".format(cor_x, cor_y))   

    def captcha_is_passed(self):
        time.sleep(3)
        try:
            img = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]')))
            if img.is_displayed():
                # self.input_captcha_again()
                print("验证未通过")
                return False
            else:
                print("验证通过")
                return True
        except Exception as e:
            print(e)
            print("验证码验证失败")
            exit(0)



    

        # print(pic_id, pic_str)

        

if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()
    crack.login()
"""
"""