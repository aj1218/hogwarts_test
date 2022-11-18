# import pytest
#
# class TestDome():
#     def test_one(self):
#         print("开始执行 test one 方法")
#         x='this'
#         pytest.assume('xx' in 'ssddwcxx')
#         pytest.assume(1 == 1)
#         pytest.assume('x'  in 'ssddwcxx')
#
#     def test_two(self):
#         print("开始执行 test two 方法")
#         x = 'thise'
#         assert 'e' in x
#
# def test_three():
#     print("开始执行 test three 方法")
#     a = 'hello'
#     b = 'hello wrod'
#     assert a not in b
import json
import time

import allure
from selenium import webdriver
import pytest
@allure.testcase("https://note.youdao.com/web/#/file/recent/note/WEBf8ee7dd7a2b6752790083f12556381a9/")
@allure.feature("百度搜索")

@pytest.mark.parametrize('test_data', ["allure", "pytest", "unittest"])
def test_steps_dmeo(test_data):
    driver = webdriver.Chrome()
    with allure.step("打开网页"):
        driver.get('http://www.baidu.com')
        driver.maximize_window()

    with allure.step(f"输入搜索词:,{test_data}"):
        driver.find_element('id','kw').send_keys(test_data)
        time.sleep(2)
        driver.find_element('id',"su").click()
        time.sleep(2)
    with allure.step("保存图片"):  #测试步骤说明
        driver.save_screenshot(r'D:\pythonProject\hogwarts_test\lessons\PMG\screenshot.png')
        #保存的图片插入allure保存展示
        allure.attach.file(r"D:\pythonProject\hogwarts_test\lessons\PMG\screenshot.png",attachment_type=allure.attachment_type.PNG)
        # 附件 描述
        allure.attach('<head></head><body>首页</body>','Attach with HTML type', attachment_type=allure.attachment_type.HTML)
        allure.attach(body="这是一段文本,teardown", name="test文本02", attachment_type=allure.attachment_type.TEXT)
    with allure.step("退出浏览器"):
        driver.quit()

if __name__ == '__main__':
    pytest.main()


