import pytest


# def pytest_collection_modifyitems(items):
#     print('pytest 收集到的所有测试用例：\n', items)
#     for item in items:
#         print('---' * 10)
#         print('用例名：', item.name)
#         print('用例节点：', item.nodeid)


# def pytest_collection_modifyitems(session, config, items):
    # print(items)
    # print(type(items))
    # #将pytest中 def中的方法类 包含add的方法 加上mark标签
    # for item in items:
    #     if 'add' in item.nodeid:
    #         item.add_marker(pytest.mark.add)
    #     # 将pytest中 def中的方法类 包含div的方法 加上mark标签
    #     elif 'div' in item.nodeid:
    #         item.add_marker(pytest.mark.div)

    # 把现有的顺序 倒序
    # items.reverse()
