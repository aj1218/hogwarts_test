from pytest_web.selenium_wxwork_login.index import Index


class TestReister:

    def setup(self):
        self.index=Index()


    def test_register(self):
        # self.index.goto_login().goto_register().register()
        self.index.goto_register().register()

