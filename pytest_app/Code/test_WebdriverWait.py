import pytest
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.webdriver.common.by import By

from pytest_app.Code.base import Base
from pytest_app.Code.load_yaml import YamlHandler

read_data = YamlHandler('../Code/testyaml.yaml').read_yaml()


class TestWebdriverWait(Base):

    @pytest.mark.parametrize('testcase',read_data["add"])
    def test_search(self,testcase):
        '''
        setup是这个方法在运行得时候就会去调用一次 setupclass是在这个类在调用得时候运行一次
        可以使用不用得setup可以减少运行时间
        1:打开雪球app
        2:点击搜索
        3:输入 搜索词 "alibaba" or "xioami"
        4:点击第一个搜索结果
        5:判断股票价格
        '''
        self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys(testcase["searchkey"])
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/name']").click()
        price = float(self.driver.find_element(MobileBy.XPATH,
                                               f'//*[@text="{testcase["type"]}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)
        expect_price = testcase["price"]
        assert_that(price,close_to(expect_price,expect_price*30))
        self.driver.back()

    def test_search1(self):
        '''
        :return:
        1:打开雪球app
        2:点击搜索
        3:输入 搜索词 "alibaba" or "xioami"
        4:点击第一个搜索结果
        5:判断股票价格
        '''
        self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys("xiaomi")
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/name']").click()
        price = float(self.driver.find_element(MobileBy.XPATH,
                                               f'//*[@text="01810"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)
        expect_price = 10
        assert_that(price, close_to(expect_price, expect_price * 30))









