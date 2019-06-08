class Person(object):

	def __init__(self, age):
		# 直接这样写是对外暴露的
		# self.age = age
		#限制访问
		self.__age = age
		# 像下面这样写是可以实现功能的，但是调用太麻烦
		'''
	def getAge(self):
		return self.__age
	def setAge(self,age):
		if age < 0:
			age = 0
		self.__age = age
	# 我们希望调用的时候还是使用最原始的方法调用，同时达到不暴露并且限制，我们可以使用@property
    # 方法名为受限制的变量去掉双下划线	'''

	@property
	def age(self):
		return self.__age
	@age.setter
	def age(self,age):
		if age < 0:
			age = 0
		self.__age = age

# 调用方便，但是对于代码是不安全的，这样是可以随意修改的
# per = Person(19)
# print(per.age)

#为了代码安全，我们必须要限制用户访问到我们不想要用户知道的信息，例如账号密码
# 采取措施：在定义类的时候在方法前面加上双下划线
#但是加了双下划线之后再像之前那样调用是不行的，解决措施：再写两个方法，一个是getAge(),一个是setAge()
# per = Person(21)
# print(per.getAge())
# per.setAge(18)
# print(per.getAge())

# 现在就可以达到目的并且以原始方法调用
per = Person(23)
print(per.age)
per.age = -100
print(per.age)


# 总结：@property可以使受限制的属性通过点语法调用