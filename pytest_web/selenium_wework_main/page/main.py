from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pytest_web.selenium_wework_main.page.add_menber import Addmenber
from pytest_web.selenium_wework_main.page.base_page import BasePage
from pytest_web.selenium_wework_main.page.phone_contactsipa import Contactsipa


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_menber(self):
        #使用围魏救赵的方法在点击通讯录之后 点击添加成员 如果添加成员中的username元素一直没有找到就一直点击添加成员
        #找到username属性之后 返回element_len > 0 结束显示等待中的死循环,直接添加成员
        # click add menber  点击添加成员
        # 如果使用隐式等待还是没有找到这个元素可以找这个元素的旁边的元素使用旁敲侧听的方式实现
        self._driver.find_element(By.ID, 'menu_contacts').click()

        def wait_add_len(x):
            # 如果没有找打username元素 就一直去点击 添加成员这个元素 如果知道了 就说明已经添加了添加成员进入了添加成员的页面
            element_len = len(self.finds(By.ID, 'username'))
            if element_len <= 0:
                # 点击添加成员
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return element_len > 0
        self.wait_for_elem(wait_add_len)
        return Addmenber(self._driver)

    def goto_phone(self):
        # click menu_contacts
        self.wait_for((By.ID, 'menu_contacts'))
        self._driver.find_element(By.ID, 'menu_contacts').click()
        return Contactsipa(self._driver)


    def goto_phone_add(self):
        # click menu_contacts
        self.wait_for((By.CSS_SELECTOR, '.index_service_cnt a:nth-child(1)'))
        self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt a:nth-child(1)').click()
        return Addmenber(self._driver)
