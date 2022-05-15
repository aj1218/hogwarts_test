import pytest

from pytest_web.testCode.base import Base
from selenium import webdriver
# from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ChromeOptions

class TestJs(Base):
    @pytest.mark.skip
    def test_js_test(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,"kw").send_keys("selenium测试")
        ele=self.driver.execute_script(' return document.getElementById("su")')
        ele.click()
        #滑动到页面的指定范围要是页面的距离小于这个 就是滑动到页面的最低端
        self.driver.execute_script("document.documentElement.scrollTop=1000")
        sleep(4)
        self.driver.find_element(By.XPATH,'//*[@id="page"]/div/a[9]/span').click()
        sleep(3)
        print(self.driver.execute_script("reture document.title;return JSON.stringify(prefoamance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_ele=self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))


