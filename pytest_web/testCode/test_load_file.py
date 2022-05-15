from time import sleep

from selenium.webdriver.common.by import By

from pytest_web.testCode.base import Base


class TestLoadFile(Base):

    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element(By.XPATH,'//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.ID,'stfile').send_keys(r'D:\pythonProject\hogwarts_test\lessons\PMG\screenshot.png')
        sleep(3)
        


