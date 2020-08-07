import time
from appium import webdriver


class Subtracting():

    def __init__(self):
        '''

               platformVersion: 填写虚拟机的版本
               deviceName: 填写安卓虚拟机的设备名称
               appPackage: 填写被测试包名
               appActivity: 填写被测试app入口
               udid: 填写通过命令行 adb devices 查看到的 uuid

               '''
        # self.driver=driver
        self.des = {

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

    def add(self, driver):
        driver = driver
        driver = driver
        driver.implicitly_wait(100)
        # 点击1
        time.sleep(3)
        driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        time.sleep(3)
        # 点击+
        driver.find_element_by_xpath('//android.widget.Button[@content-desc="加"]').click()
        time.sleep(3)
        # 点击3
        driver.find_element_by_xpath('//android.widget.Button[starts-with(@text,3)]').click()
        time.sleep(3)
        # 点击 =
        driver.find_element_by_xpath('//android.widget.Button[@content-desc="等于"]').click()

    def subtraction(self, driver):
        driver = driver
        time.sleep(3)
        # 绝对路径 定位元素3
        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Button[3]').click()
        # time.sleep(3)
        # 属性定位 定位元素-
        driver.find_element_by_xpath('//android.widget.Button[@content-desc="减"]').click()
        # time.sleep(3)
        # 部分属性定位 定位元素1
        driver.find_element_by_xpath('//android.widge0t.Button[starts-with(@text,1)]').click()
        # time.sleep(3)
        # 属性定位 定位元素=
        driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/eq"]').click()

    def multiplication(self, driver):
        driver = driver
        time.sleep(3)
        # 属性定位 定位元素6
        driver.find_element_by_xpath(
            '//android.widget.Button[@resource-id="com.android.calculator2:id/digit_6"]').click()
        time.sleep(3)
        # 定位元素x
        driver.find_element_by_xpath('//android.widget.Button[@text="×"]').click()
        # time.sleep(3)
        # 部分属性定位 定位元素2
        driver.find_element_by_xpath(
            '//android.widget.Button[contains(@resource-id,com.android.calculator2:id/digit_2)]').click()
        time.sleep(3)
        # 部分属性定位 定位元素=
        driver.find_element_by_xpath('//android.widget.Button[@content-desc="等于"]').click()

    def division(self, driver):
        driver = driver
        time.sleep(3)
        # 属性定位 定位元素6
        driver.find_element_by_xpath(
            '//android.widget.Button[@resource-id="com.android.calculator2:id/digit_8"]').click()
        time.sleep(3)
        # 定位元素x
        driver.find_element_by_xpath('//android.widget.Button[@text="÷"]').click()
        # time.sleep(3)
        # 部分属性定位 定位元素4
        driver.find_element_by_xpath(
            '//android.widget.Button[@resource-id="com.android.calculator2:id/digit_2"]').click()
        time.sleep(3)
        # 部分属性定位 定位元素=
        driver.find_element_by_xpath('//android.widget.Button[@content-desc="等于"]').click()

    def start_appium(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.des)
        return driver


if __name__ == "__main__":
    driver = Subtracting().start_appium()
    appium_start = Subtracting().add(driver)
