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

# 1、利用xpath的识别方式，使用 属性 定位、部分属性值定位 来完成计算机的相关加减乘除功能
# 【减法】
# time.sleep(3)
# 绝对路径 定位元素9
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Button[3]').click()
# time.sleep(3)
# 属性定位 定位元素-
# driver.find_element_by_xpath('//android.widget.Button[@content-desc="减"]').click()
# time.sleep(3)
#部分属性定位 定位元素1
# driver.find_element_by_xpath('//android.widge0t.Button[starts-with(@text,1)]').click()
# time.sleep(3)
#属性定位 定位元素=
# driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/eq"]').click()

#【加法】

# time.sleep(3)
# 属性定位 定位元素9
# driver.find_element_by_xpath('//android.widget.Button[@text="6"]').click()
# time.sleep(3)
# 属性定位 定位元素+
# driver.find_element_by_xpath('//android.widget.Button[@content-desc="加"]').click()
# time.sleep(3)
#部分属性定位 定位元素3
# driver.find_element_by_xpath('//android.widget.Button[contains(@resource-id,digit_3)]').click()
# time.sleep(3)
#部分属性定位 定位元素=
# driver.find_element_by_xpath('//android.widget.Button[@content-desc="等于"]').click()


# 【乘法】


#
# time.sleep(3)
# # 属性定位 定位元素6
# driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/digit_6"]').click()
# time.sleep(3)
# # 定位元素x
# driver.find_element_by_xpath('//android.widget.Button[@text="×"]').click()
# # time.sleep(3)
# # 部分属性定位 定位元素4
# driver.find_element_by_xpath('//android.widget.Button[contains(@resource-id,com.android.calculator2:id/digit_2)]').click()
# time.sleep(3)
# # 部分属性定位 定位元素=
# driver.find_element_by_xpath('//android.widget.Button[@content-desc="等于"]').click()


# 【除法】


time.sleep(3)
# 属性定位 定位元素6
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/digit_8"]').click()
time.sleep(3)
# 定位元素x
driver.find_element_by_xpath('//android.widget.Button[@text="÷"]').click()
# time.sleep(3)
# 部分属性定位 定位元素4
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/digit_2"]').click()
time.sleep(3)
# 部分属性定位 定位元素=
driver.find_element_by_xpath('//android.widget.Button[@content-desc="等于"]').click()
