from time import sleep

from pytest_web.testCode.base import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlert(Base):
    def test_Alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        sleep(3)
        self.driver.switch_to_frame('iframeResult')
        darp=self.driver.find_element(By.ID,'draggable')
        drop=self.driver.find_element(By.ID,'droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(darp,drop).perform()
        sleep(3)
        print("对alert弹窗点击确认")
        self.driver.switch_to.alert.accept()   #对alert弹窗点击确认
        self.driver.switch_to.default_content()  #返回默认的switch弹窗

        self.driver.find_element(By.ID,'submitBTN').click()
        sleep(3)

