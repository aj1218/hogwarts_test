from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

# 这是一个添加成员的PO
from pytest_web.selenium_wework_main.page.base_page import BasePage


class Addmenber(BasePage):

    def add_menber(self):
        # sendkeys
        self.find(By.ID, "username").send_keys('name219')
        # self.find(By.ID, "memberAdd_english_name").send_keys("3211208")
        self.find(By.ID, "memberAdd_acctid").send_keys("zhang1hao208")
        self.find(By.ID, "memberAdd_phone").send_keys("13121111387")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def page(self):
        # 得到当前页的分页的数据 获取到当前分页的文本  1/10
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        # 使用python自带的分割 得到页数的 当前页和总页数的数据  使用斜杠作为分隔符 切割一次得到一个list list[0]=1 list[1]=10
        # 强行把得到的list分页数据 转换为int类型 使用for循环遍历list数据改为数组
        return [int(x) for x in content.split('/', 1)]


    def get_menber(self,value):  #传值做判断 不用每一个都把数据追加到list里面去
        self.wait_for((By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)'))
        cur_page, total_page = self.page()
        #提取出来之后使用死循环遍历数据
        while True:
            #获取 通讯录中的姓名列
            elements = self.finds(By.CSS_SELECTOR, '.member_colRigh t_memberTable_td:nth-child(2)')
            # 使用循环得到每一页的title 也就是姓名的数据
            for element in elements: # 使用判断 如果获取元素组中有传进来的那个元素 直接返回True
                if value == element.get_attribute("title"):
                    return  True
            # 更新当前页数据
            cur_page = self.page()[0]
            # 如果当前页的数据等等于总页数 就说明到了页尾
            if cur_page == total_page:
                # 如果到了页尾都没找到这个元素 直接返回False 就是没有找到这个元素
                return False
            # 点击当前页面的分页数据 下一页的数据 如果不等于
            self.find(By.CSS_SELECTOR,'.js_next_page').click()
            # # 如果当前页的页数小于总页数
            # if cur_page < total_page:
            #     # 就去替换当前页的数据 cur_page 更新当前页
            #     cur_page= [int(x) for x in content.split('/', 1)][0]

            # for element in elements:
            #     list.append(element.get_attribute("title"))
            # return list
        # return [element.get_attribute("title") for element in elements] #上面方式的简洁版本
