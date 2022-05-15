from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_ActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_case_actionchains(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        elmen_click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        elmen_douleclick = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        elmen_rightclick = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(elmen_click)  # 点击
        action.context_click(elmen_rightclick)  # 右键
        action.double_click(elmen_douleclick)  # 双击
        sleep(3)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_movetoelment(self):
        self.driver.get("https://www.baidu.com/?tn=02003390_19_hao_pg")
        ele=self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        action=ActionChains(self.driver)
        action.move_to_element(ele)   #鼠标悬停事件
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragDrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele=self.driver.find_element(By.ID,'dragger')
        drop_ele=self.driver.find_element(By.XPATH,"/html/body/div[2]")
        action=ActionChains(self.driver)
        action.drag_and_drop(drag_ele,drop_ele)   #点击一个元素不放 放在下一个元素中
        action.perform()
        sleep(5)

    def test_keys(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        drop_ele=self.driver.find_element(By.XPATH,"/html/body/label[1]/input").click()
        action=ActionChains(self.driver)
        action.send_keys("usrname").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE)
        action.perform()
        sleep(5)

if __name__ == '__main__':
    pytest.main()
