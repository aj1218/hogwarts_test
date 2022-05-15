from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):  # driver:WebDriver 告诉python这个参数一个webdriver类型的 使用这个参数的时候 可以点出这个类型里面的方法
        # 为了不重写driver 可以直接复用上一个类里面的driver 就是index页面的driver
        self._driver = driver

    def register(self):
        sleep(5)
        self._driver.find_element(By.ID,'corp_name').send_keys("hello111")
        self._driver.find_element(By.ID,'manager_name').send_keys("name")
        sleep(5)
        self._driver.quit()
        return True



