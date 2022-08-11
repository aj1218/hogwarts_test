import logging

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from appium_xueqiu.page.wrapper import headle_black


class BasePage:
    _params = {}
    # 弹框 处理的定位列表
    logging.basicConfig(level=logging.INFO)


    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements


    @headle_black
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        # element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
        #     locator, value)
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element

    def steps(self, path, encoding='utf-8'):
        with open(path, encoding=encoding) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
