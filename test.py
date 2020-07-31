import time
from appium import webdriver

des={


    'platformName':'Android',
    'platformVersion': '6.0.1',#填写虚拟机的版本
    'deviceName':  'android',#填写安卓虚拟机的设备名称
    'appPackage':'com.android.calculator2'  , #填写被测试包名
    'appActivity':'.Calculator', #填写被测试app入口
    'udid': '192.168.206.102:5555',  # 填写通过命令行 adb devices 查看到的 uuid
    'automationName': 'UiAutomator1',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True

}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
driver.implicitly_wait(1000)

#点击9
# driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
# 点击删除
# driver.find_element_by_accessibility_id('删除').click()

#点击1
time.sleep(3)
driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
time.sleep(3)
#点击0
driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
time.sleep(3)
# 点击+
driver.find_element_by_accessibility_id('加').click()
time.sleep(3)
# 点击5
driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
time.sleep(3)
#点击 =
driver.find_element_by_accessibility_id('等于').click()
