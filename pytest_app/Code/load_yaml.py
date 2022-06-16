import yaml


class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read_yaml(self, encoding='utf-8'):
        """读取yaml数据,Loader=yaml.FullLoader这个必须得加上更加安全，不加报错"""
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding='utf-8'):
        """向yaml文件写入数据"""
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    data = {
        "user": {
            "username": "vivi",
            "password": "123456"
        }
    }
    # 读取config.yaml配置文件数据
    read_data = YamlHandler('../Code/testyaml.yaml').read_yaml()
    # 将data数据写入config1.yaml配置文件
    # write_data = YamlHandler('../Code/testyaml.yaml').write_yaml(data)
    if "alibaba" in read_data:
        print("2222")
    else:
        print("3")