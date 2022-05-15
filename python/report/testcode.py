# all方法:在方法中使用all方法  然后使用import * 才能使用all方法的特性 all的意思就是:对外公开的数据,没有写在all里面的在import * 是不能直接使用的

# __all__ = ['f']
# hello = "hello dome1"


class Dome1:
    def add(self, a, b):
        return a + b

    def dev(self, a, b):
        return a - b
