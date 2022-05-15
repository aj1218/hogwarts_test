import pytest


class TestDome:

    @pytest.fixture()
    def login(self):
        print("需要登录")
        uername="tom"
        yield uername
        print("downdraft")

    def test_a(self,login):
        # 第一步:打开浏览器
        # 第二步 输入网址
        # 第三步  定位
        # 第四步 各种操作
        # 第五步 关闭浏览器
        print(login)

        print("test_a")

    def test_b(self):
        print("test_b")

    # def test_c(self):
    #     pass
