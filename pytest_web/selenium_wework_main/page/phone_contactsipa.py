from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pytest_web.selenium_wework_main.page.add_menber import Addmenber
from pytest_web.selenium_wework_main.page.base_page import BasePage


class Contactsipa(BasePage):

    def phone_contactsipa(self):
        # self.wait_for((By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)"))
        self.wait_for_elem(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member")))
        self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
        return Addmenber(self._driver)
