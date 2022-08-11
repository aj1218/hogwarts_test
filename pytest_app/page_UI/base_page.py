import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _params = {}
    _blank_list = [(By.ID, "iv_action_back")]

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

    def find(self, locator, value: str = None):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            for bick in self._blank_list:
                elements = self._driver.find_elements(*bick)  # 找黑名单里面得元素
                if len(elements) > 0:
                    elements[0].click()  # 如果找到了 就对这个元素点击
                    break  # 点击之后退出循环
            # 处理黑名单之后再次找原来得元素
            return self.find(locator, value)
        # element: WebElement
        # if isinstance(locator, tuple):
        #     element = self._driver.find_element(*locator)
        # else:
        #     element = self._driver.find_element(locator, value)
        #
        # return element

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


if __name__ == '__main__':
    steps = BasePage()
    step = steps.steps(r"D:\pythonProject\hogwarts_test\pytest_app\page_UI\main.yaml")
    print(step)
