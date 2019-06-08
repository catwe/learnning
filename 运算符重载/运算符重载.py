#不同的数据类型使用‘+’运算符的结果是不同的
print(1 + 2)
print('1'+'2')

class Person(object):
	def __init__(self,num):
		self.num = num
		# 重写__add__方法
	def __add__(self, other):
		return Person(self.num + other.num)
	# 重写字符串
	def __str__(self):
		return "num = " + str(self.num)

per1 = Person(1)
per2 = Person(2)
print(per1.num)
print(per2.num)
# 现在我们想要这个两个对象相加，但是直接像下面这样写是错误的
# print(per1 + per2)
# 此时，我们就需要在类里面重写‘+’的定义
print(per1 + per2)  #直接这样写会返回一个地址<__main__.Person object at 0x0000013497EE3E10>，所以我们还需要重写字符串
print(per2)
print(per1)


# 总结：运算符重载的目的是改写已有的运算符方法达到我们想要的目的