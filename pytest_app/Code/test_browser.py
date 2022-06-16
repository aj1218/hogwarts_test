from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testbrowser:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62001",
            "browserName" : "Browser",
            "noReset": True,
            "dontStopAppOnReset": True,  # 不退出App
            # "chromedriverExecutable": r"D:\pythonProject\hogwarts_test\chromedriver.exe",  # 指定driver地址
            "automationName": "Uiautomator2",
            "skipDeviceInitialization": True,  # 权限
            "unicodeKeyboard": True,  # 这个和下面那个 这两个关键字是控制中文的输入的
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com/")
        self.driver.find_element(By.CLASS_NAME,'fake-placeholder').click()
        self.driver.find_element(By.ID, 'index-kw').send_keys("appium")
        self.driver.find_element(By.ID,"index-bn").click()
        sleep(4)

