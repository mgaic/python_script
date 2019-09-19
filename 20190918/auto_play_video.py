from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import TimeoutException
import time
import random

class DouYinVideo(object):
    def __init__(self):

        self.cap = {
          "platformName": "Android",
          "platformVersion": "8.0.0",
          # "platformVersion": "5.1.1",
          # "deviceName": "MKJ4C18802001823",
          "deviceName": "MKJ4C18802001823",
          # "deviceName": "192.168.43.4:6666",
          "appPackage": "com.ss.android.ugc.aweme.lite",
          "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
          "noReset": True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.cap)
    
    def slide_play(self):
        while True:
          sleep_time = random.normalvariate(8, 10) #每个视频大致停留8s总有，总体停留时间服从正态分布
          if (sleep_time > 2) and (sleep_time < 14):
              print("正在播放...{}秒后切换视频".format(sleep_time))
              time.sleep(sleep_time)
              
              break
        screen_height = self.driver.get_window_size()['height']
        screen_width = self.driver.get_window_size()['width']
        start_x = random.randint(int(screen_width * 0.3), int(screen_width * 0.5))
        start_y = random.randint(int(screen_height * 0.65),int(screen_height * 0.8))
        end_x = start_x + random.randint(int(screen_width * 0.07), int(screen_width * 0.1))
        end_y = start_y - random.randint(int(screen_height * 0.18), int(screen_height * 0.25))
        duration = random.randint(280,480)
        print(start_x, ',', start_y)
        print(end_x, ',', end_y)
        print("duration is", duration)
        self.driver.swipe(start_x, start_y, end_x, end_y, duration = duration)
    
douyin_object = DouYinVideo()
for i in range(20):
    douyin_object.slide_play() #滑动播放20个视频



