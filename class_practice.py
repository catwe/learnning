class Student(object):          #定义一个类，类名为Student
	count = 0
	def __init__(self,name,score):          #类的属性绑定，也是函数，也叫方法，但是首个参数必须为self
		self.name = name
		self.score = score
		Student.count += 1
	def print_score(self):                  #定义一个方法
		print('%s:%s'%(self.name,self.score))
	def getgrade(self):
		if self.score>=90:
			return 'A'
		elif self.score>=80:
			return 'B'
		elif self.score>=60:
			return 'C'
		else:
			return 'OUT!!'


bart = Student('Wangcong', 89)
andy = Student('andy',20)
print(bart.print_score(),bart.getgrade())
print(andy.print_score(),andy.getgrade())



#访问限制练习    __变量名  为内部变量，外部不可访问，如需访问，可以定义  get_变量名 如需修改，定义set_变量名方法
class Staff(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender =gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender
dili = Staff('Bart', 'male')
if dili.get_gender() != 'male':
    print('测试失败!')
else:
    dili.set_gender('female')
    if dili.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')




#继承、多态练习
class Animal(object):
	def run(self):
		print('Animal is running.....')

animal = Animal()
print(animal.run())

class Cat(Animal): #Animal的子态
	def run(self):   #与父态相同的方法将会覆盖父态的方法
		print('Cat is running...')

class Dog(Animal):
	pass
# def run(self):
		# print('Dog is running..')


dog = Dog()
print(dog.run())

from enum import Enum,unique

Gender=Enum('Gender',('Male','Female'))
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender