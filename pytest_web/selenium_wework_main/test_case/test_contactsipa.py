from time import sleep

from pytest_web.selenium_wework_main.page.main import Main


class TestContactsipa:
    def setup(self):
        self.main=Main()

    def test_contactsipa(self):
        #两种验证方式 第一种是使用围魏救赵的方式 第二个是使用显示等待元素是否展示
        contactsipa = self.main.goto_add_menber()
        # contactsipa = self.main.goto_phone().phone_contactsipa()
        contactsipa.add_menber()
        assert contactsipa.get_menber("张三13")

