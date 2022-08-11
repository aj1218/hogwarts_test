
import yaml

# # print(yaml.dump(open("test.yaml")))
# with open("test.yaml","w") as f:
#     w={'a': [1, 2]}
#     yaml.dump(w,f)
#     print(yaml.dump(w,f))
from pytest_app.Code.load_yaml import YamlHandler

read_data = YamlHandler(r'D:\pythonProject\hogwarts_test\python\testing\datas\test.yaml').read_yaml()
print(read_data)