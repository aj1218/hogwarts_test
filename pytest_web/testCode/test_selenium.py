from time import sleep

import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("https://home.testing-studio.com/")
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()

    def testSelenium(self):
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("python")
        # self.driver.find_element(By.CSS_SELECTOR, "#s_tab a:nth-child(2)").click()
        # self.driver.find_element(By.CSS_SELECTOR, '[title="所有分类"]').click()
        # sleep(3)
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) > 1
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        # self.driver.find_element(By.XPATH,'//*[@title="过去一年、一个月、一周或一天中最活跃的话题"]').click()




