class Person(object):
	name = '这是类属性'
	def __init__(self, name):
		# pass
		#这是对象属性
		self.name = name

#调用
per = Person('tom')
#调用对象属性，对象属性优先级高于类属性，当属性名相同时，对象属性作用优先
print(per.name)

#调用类属性
print(Person.name)

#动态的添加属性，但是只作用于本对象，例如添加一个per2对象时，动态添加的属性不会作用
per.age = 21
print(per.age)

# per2 = Person('wc')
#调用age属性就会报错
# print(per2.age)

#注意：千万不要将对象属性和类属性重名，因为对象属性会屏蔽类属性，
# 但是当删除掉对象属性后，调用同名属性时，就会调用到类属性。
