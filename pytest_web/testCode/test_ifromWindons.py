from selenium.webdriver.common.by import By
from time import sleep

from pytest_web.testCode.base import Base


class TestWindows(Base):
    def test_ifram_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.LINK_TEXT,"登录").click()
        self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys("123")
        sleep(2)
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__phone').send_keys("15611111111")
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__password').send_keys("123456")




