
import time
from appium import webdriver
class ComputerAddition():
    def __init__(self):

        '''

        platformVersion: 填写虚拟机的版本
        deviceName: 填写安卓虚拟机的设备名称
        appPackage: 填写被测试包名
        appActivity: 填写被测试app入口
        udid: 填写通过命令行 adb devices 查看到的 uuid

        '''
        # self.driver=driver
        self.des={

            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'deviceName': 'android',
            'appPackage': 'com.android.calculator2',
            'appActivity': '.Calculator',
            'udid': '192.168.206.102:5555',
            'automationName': 'UiAutomator1',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True

        }

    def computeraddition(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(100)
        # 点击1
        time.sleep(3)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        time.sleep(3)
        # 点击0
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        time.sleep(3)
        # 点击+
        self.driver.find_element_by_accessibility_id('加').click()
        time.sleep(3)
        # 点击5
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        time.sleep(3)
        # 点击 =
        self.driver.find_element_by_accessibility_id('等于').click()

    def start_appium(self):
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.des)
        return driver

if __name__=="__main__":
    dri=ComputerAddition().start_appium()
    driver=ComputerAddition().computeraddition(dri)

