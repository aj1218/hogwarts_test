from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import assert_that, equal_to, close_to, contains_string


class TestDW:

    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            # "dontStopAppOnReset": True,  # 不退出App
            "automationName": "Uiautomator2",
            "skipDeviceInitialization": True,  # 权限
            "unicodeKeyboard": True,  # 这个和下面那个 这两个关键字是控制中文的输入的
            "resetKeyboard": True

        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):

        self.driver.quit()

    def test_search(self):
        print("搜索的测试用例")
        """
        1:打开雪球app
        2:点击搜索
        3:像搜索输入框中输入"阿里巴巴"
        4:在搜索结果中选择"阿里巴巴",进行点击
        5:获取这只上香港 阿里巴巴的股价 并判断这是股价的价格>200
        
        """
        self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()
        sleep(1)
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element(By.ID, 'com.xueqiu.android:id/current_price').text)

        assert_that(current_price,close_to(87,10))

    def test_attr(self):
        """
        打开雪球app
        定位首页的搜索框
        判断搜索框是否可用 并查看搜索框的name属性值
        打印搜索框这个元素的左上角坐标和他的宽高
        向搜索框输入 :alibaba
        判断alibaba 是否可见
        如果可见 打印搜索成功 点击 如果不可见 打印搜索失败
        :return:
        """
        elemen = self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search")
        search_enabled = elemen.is_enabled()  # 是否可用
        print("", elemen.text)  # 获取搜索框中的文本属性
        print(elemen.location)  # 左上角坐标
        print(elemen.size)  # 宽高
        if search_enabled == True:
            elemen.click()
            alibaba_elenent = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys(
                "阿里巴巴")
            # alibaba_elenent.is_displayed()  # 判断阿里巴巴是否可见
            elment_displayed = alibaba_elenent.get_attribute("displayed")  # 判断这个元素是否可见
            if elment_displayed == "true":
                print("搜索成功")
            else:
                print("搜索失败")
        else:
            print("输入框元素不可用")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        Windows_size = self.driver.get_window_rect()  # 获取屏幕尺寸
        width = Windows_size["width"]
        height = Windows_size["height"]
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)  # 起点
        y_end = int(height * 1 / 5)  # 终点
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        # action.press(x=731,y=1083).wait(200).move_to(x=731,y=484).release().perform()   # 试用手势密码的时候 就可以使用坐标的方法一个一个定位在滑动

    def test_get_price(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        price = float(self.driver.find_element(By.XPATH,
                                               '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)
        print("当前09988对应的股票价格:", price)
        expect_price = 90
        assert_that(price,close_to(expect_price,expect_price*0.1))

    def test_toast(self):

        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.xueqiu.android:id/profile_image"]/android.widget.ImageView[1]').click()
        self.driver.find_element(By.XPATH, '//*[@text="帐号密码登录"]').click()
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/login_account"]').send_keys(
            "15388030234")
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/login_password"]').send_keys(
            "qq977089471.")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/button_next"]')))
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/button_next"]').click()
        print(self.driver.page_source)
        # print(self.driver.find_element(By.XPATH, "//*[@class='android.view.View']"))
        # self.driver.back()
        sleep(1)
        self.driver.back()
        self.test_quit()

    def test_quit(self):
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.xueqiu.android:id/profile_image"]/android.widget.ImageView[1]').click()
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_setting"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true))'
                                 f'.scrollIntoView(new UiSelector().text("退出登录"));').click()
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/md_buttonDefaultPositive"]').click()


    def test_hamrest(self):
        # assert_that(10, equal_to(1),"这是一个提示")   #比较
        assert_that(10, close_to(9,3), "这是一个提示")  # 上下浮动的空间是否包含目标数字
        # assert_that("contains some string", contains_string("string"), "这是一个提示")  # 字符串是否包含 前面那个字符串是都包含后面的字符串数据




if __name__ == '__main__':
    pytest.main()
