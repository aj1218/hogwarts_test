from time import sleep

from pytest_web.selenium_wework_main.page.main import Main


class TestAddMenber:
    def setup(self):
        self.main=Main()

    def test_addmenber(self):
        add_menber=self.main.goto_phone_add()
        add_menber.add_menber()
        sleep(2)
        assert  add_menber.get_menber("name12")

