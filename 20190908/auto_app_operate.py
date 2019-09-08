from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

cap = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ninetyone.pron.android",
  "appActivity": "com.ninetyone.pron.android.ui.LaunchActivity",
  "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

try:
	time_skip_btn = WebDriverWait(driver, 5).util(driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.Button'))
	time_skip_btn.click()
except:
	pass

try:
    advertisement_btn = WebDriverWait(driver, 5).util(driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]'))
    driver.keyevent(4)
except
    pass

try:
    advertisement_btn2 = WebDriverWait(driver, 5).util(driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ninetyone.pron.android:id/iv_close']"))
    driver.keyevent(4)
except
    pass

try:
    self_info_btn = WebDriverWait(driver, 5).util(driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ninetyone.pron.android:id/tv_main_mine']"))
    self_info_btn.click()
except
    pass

try:
    self_set_btn = WebDriverWait(driver, 5).util(driver.find_element_by_xpath("//android.widget.RelativeLayout[@resource-id='com.ninetyone.pron.android:id/relative_setting']"))
    self_set_btn.click()
except
    pass

try:
#
    write_invite_code_btn = WebDriverWait(driver, 5).util(driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ninetyone.pron.android:id/text_my_invite']"))
    write_invite_code_btn.click()
except
    pass




