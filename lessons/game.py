


# class Game:
#
#     hp = 1000
#     power = 200
#     def figth(self, enemy_power, enemy_hp):
#         final_hp = self.hp - enemy_power
#         enemy_final_hp =  enemy_hp - self.power
#         if final_hp>enemy_final_hp:
#             print("我赢了")
#         elif final_hp<enemy_final_hp:
#             print("敌人赢了")
#         else:
#             print("平局")
#
# game=Game()
# test=game.figth(1,3)



a=2j
print(type(a))



result=0
for i in range(2,151,2):
    result=result+i
print(result)

y = lambda x:x*2
print(y(2))


# *列表的特性
# list.append(x):在列表的末尾添加一个元素。相当于allen(a):1=[x]。
# list.insert(i, x):在给定的位置插入一个元素。第一个参数是要插入的元素的索引,以a.insert(0, x)插入列表头部, a.insert(len(a), x)等同于a.append(x)
# list.remove(x):移除列表中第一个值为x的元素。如果没有这样的元素,则抛出ValueError异常
# list.pop(i):删除列表中给定位置的元素并返回它。如果没有给定位置, a.pop0)将会删除并返回列中的最后一个元素
# list.sort(key-None, reverse-False):对列表中的元素进行排序(参数可用于自定义排序,解释请参见sorted())
# list.reverse():反转列表中的元素。
list_hogwarts=[]
# list_hogwarts.append(0)
# list_hogwarts.insert(0,9)
for i in range(1,9,3):
    if i!=1:
        list_hogwarts.append(i**2)
print(list_hogwarts)

print({i :i * 2 for i in range(1,4,3)})

name="yyy"
str="my name is %s,my sge is %d"%(name,20)
print(str)





















