from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class Testjiaohu:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            # "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "avd":"Android_6",  #启动android内部自建的模拟器 三方模拟器不支持
            "dontStopAppOnReset": True,  # 不退出App
            "automationName": "Uiautomator2",
            "skipDeviceInitialization": True,  # 权限
            "unicodeKeyboard": True,  # 这个和下面那个 这两个关键字是控制中文的输入的
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.back()

    def test_jiaohu(self):
        # self.driver.make_gsm_call("15612341234",GsmCallActions.CALL)
        # self.driver.send_sms("17911112222","Holle appium api")
        self.driver.set_network_connection(1)
        sleep(3)
        self.driver.set_network_connection(4)
        sleep(4)



