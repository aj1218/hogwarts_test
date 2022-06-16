
from pytest_app.Code.base import Base
from selenium.webdriver.common.by import By



class TestAttr(Base):

    def test_attr(self):
        seach_ele =self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search")
        print(seach_ele.get_attribute("content-desc"))
        print(seach_ele.get_attribute("resource-id"))
        print(seach_ele.get_attribute("bounds"))






