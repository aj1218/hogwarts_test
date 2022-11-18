import inspect
import json

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from appium_xueqiu.page.wrapper import headle_black


class BasePage:
    _params = {}
    # 弹框 处理的定位列表

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

        element: WebElement
        # element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
        #     locator, value)
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element

    @headle_black
    def find_and_get_text(self, locator, value: str = None):

        element: WebElement
        # element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
        #     locator, value)
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator)
        else:
            element_text = self._driver.find_element(locator, value)

        return element_text

    def step(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function    # 1是代表内本身  2代表调用类的人(依次往后推)
            steps = yaml.safe_load(f)[name]

            raw = json.dumps(steps)
            for key, value in self._params.items():
                raw = raw.replace('${' + key + '}', value)
            steps = json.loads(raw)
            for step in steps:
                if "action" in step.keys():
                    action = step["action"]
                    if "click" == action:
                        self.find(step["by"], step["locator"]).click()
                    if "send" == action:
                        self.find(step["by"], step["locator"]).send_keys(step["value"])
                    if "len > 0" == action:
                        eles = self.finds(step["by"], step["locator"])
                        return len(eles) > 0



