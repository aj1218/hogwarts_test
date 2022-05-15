
# yield + 函数 == 生长器

def provider():
    for i in range(0,10):
        yield i  #生成器  类似于 return i


p=provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

