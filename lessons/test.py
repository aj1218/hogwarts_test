import pytest
import yaml

class TestDome:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./test.yaml"))["add"])
    def test_demo(self,env):
        print(env)
        # if "test" in env:
        #     print("这是测试环境:",env)
        #     # print(env["name"])
        # elif "dev" in env:
        #     print("这是开发环境")
        # else:
        #     print("这是正式环境")
# def test_1():
#     print("测试")

