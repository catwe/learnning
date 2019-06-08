from types import MethodType
#创建一个空的类
class Person(object):
	__slots__ = ('name','age','height','wight','ag','agg')


# 添加属性
per = Person()
per.name = 'wangcong'
per.ag = '21 '
print(per.name)
print(per.ag)

# 添加方法
def age(self):
	# self.ag = ag
	# print('my name is :'+ self.name)
    print('my age is '+ self.ag)
per.agg = MethodType(age,per)
per.agg()


# 想要限制添加的属性，例如只能允许添加（name, age ,wight, hight等等）
# 解决办法：在定义类的时候添加一个__slots__属性，例如：
per.height = '180cm '
print(per.height)
# per.kk = '这是不允许添加的属性'
# print(per.kk)