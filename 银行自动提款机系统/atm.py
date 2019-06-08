from card import Card
from user import User
import random
import time
class ATM(object):
	def __init__(self,allUser):
		# 以字典形式存储卡号，用户
		self.allUser = allUser
	def createUser(self):
		# 目标：向用户字典中添加一对键值（卡号-用户)
		name = input('请输入您的姓名，以回车结束：')
		idCard = input('请输入您的身份证号码，以回车结束：')
		if len(idCard) != 18:
				for i in range(3):
					idCard = input('身份证为十八位，您输入有误，请重新输入（3次机会）：')
					if len(idCard) == 18:
						break
				if len(idCard) != 18:
					return -1

		phone = input('请输入您的11位电话号码，以回车结束：')
		if len(phone) != 11:
			for i in range(3):
				phone = input('您输入的电话号码不是11位，请重新输入(3次机会)：')
				if len(phone) == 11:
					break
			if len(phone) != 11:
				return -1

		prestoreMoney = int(input('请输入预存款金额：'))
		if prestoreMoney< 0:
			print('预存款输入有误，开户失败！！')
			time.sleep(3)
			return -1
		onePasswd = input('请设置密码：')
		# 密码验证
		if not self.checkPasswd(onePasswd):
			print('您输入的密码错误，开户失败......')
			time.sleep(3)
			return -1
		# 所有需要的信息就全了
		cardStr = self.randomCardId()

		card = Card(cardStr, onePasswd, prestoreMoney)
		user = User(name, idCard, phone, card)
		self.allUser[cardStr] = user
		print('恭喜您!开户成功......')
		time.sleep(1)
		print('请牢记您的卡号：'+ cardStr)
		time.sleep(3)

	def searchUserInfo(self):
		#查询
		cardNum = input('请输入您要查询的卡号，并以回车结束：')
		# 验证卡号是否存在
		cuser = self.allUser.get(cardNum)
		if not cuser:
			print('该卡号不存在，查询失败>>>>>>')
			return -1
		if cuser.card.cardID == 0:
			print('此卡已被销户，查询失败......')
			return -1

		# 验证是否锁定
		if cuser.card.cardLock:
			print('该卡已被锁定，请解锁后进行其他操作......')
			return -1

		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，该卡已被锁定，请解锁后进行其他操作>>>>>>')
			cuser.card.cardLock = True
			return -1
		print('恭喜!!查询成功>>>>>')
		print('尊敬的:%s 先生/女士，您的账户信息如下：'%cuser.name)
		print('……………账号：%s    余额：%d…………'%(cuser.card.cardID,cuser.card.cardMoney))

	def getMoney(self):
		# 取款
		cardNum = input('请输入您要取款的卡号，并以回车结束：')
		# 验证卡号是否存在
		cuser = self.allUser.get(cardNum)
		if cuser.card.cardID == 0:
			print('此卡已被销户，取款失败......')
			return -1
		if not cuser:
			print('该卡号不存在，取款失败>>>>>>')
			return -1
		# 验证是否锁定
		if cuser.card.cardLock:
			print('该卡已被锁定，请解锁后进行其他操作......')
			return -1

		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，该卡已被锁定，请解锁后进行其他操作>>>>>>')
			cuser.card.cardLock = True
			return -1
		money = int(input('请输入取款金额：'))
		if money > cuser.card.cardMoney:
			print('余额不足!!取款失败......')
			return -1
		if money <= 0:
			print('输入错误!!取款失败......')
			return -1
		cuser.card.cardMoney -= money
		print('取款成功!!余额为：%d'%(cuser.card.cardMoney))








	def saveMoney(self):
		# 存款
		cardNum = input('请输入您要存储的卡号，并以回车结束：')
		# 验证卡号是否存在
		cuser = self.allUser.get(cardNum)
		if cuser.card.cardID == 0:
			print('此卡已被销户，存款失败......')
			return -1
		if not cuser:
			print('该卡号不存在，存款失败>>>>>>')
			return -1
		# 验证是否锁定
		if cuser.card.cardLock:
			print('该卡已被锁定，请解锁后进行其他操作......')
			return -1

		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，该卡已被锁定，请解锁后进行其他操作>>>>>>')
			cuser.card.cardLock = True
			return -1
		money = int(input('请输入存款金额：'))
		if money <= 0:
			print('输入错误!!存款失败......')
			return -1
		cuser.card.cardMoney += money
		print('存款成功!!余额为：%d' % (cuser.card.cardMoney))


	def tansferMoney(self):
		# 转账
		cardNum = input('请输入您要登陆的卡号，并以回车结束：')
		# 验证卡号是否存在
		cuser = self.allUser.get(cardNum)
		if cuser.card.cardID == 0:
			print('此卡已被销户，转账失败......')
			return -1
		if not cuser:
			print('该卡号不存在，登陆失败>>>>>>')
			return -1
		# 验证是否锁定
		if cuser.card.cardLock:
			print('该卡已被锁定，请解锁后进行其他操作......')
			return -1

		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，该卡已被锁定，请解锁后进行其他操作>>>>>>')
			cuser.card.cardLock = True
			return -1
		people = input('请输入你想要转账用户的卡号，以回车结束：')
		peopleCardId = self.allUser.get(people)
		if not peopleCardId:
			print('该卡号不存在，转账失败>>>>>>')
			return -1
		# 验证是否锁定
		if peopleCardId.card.cardLock:
			print('该卡已被锁定，请解锁后进行其他操作......')
			return -1

		money = int(input('请输入转账金额：'))
		if money > cuser.card.cardMoney:
			print('您的余额不足!!转账失败.......')
			return -1

		if money <= 0:
			print('输入错误!!转账失败......')
			return -1

		judge = input('是否转账给'+ peopleCardId.name + '先生/女士？回复：（yes/no）：')
		if judge == 'yes':
			cuser.card.cardMoney -= money
			peopleCardId.card.cardMoney += money
			print('存款成功!!余额为：%d' % (cuser.card.cardMoney))
			time.sleep(1)
			print('到账成功!!对方余额为：%d' % (peopleCardId.card.cardMoney))
		if judge == 'no':
			print('退出转账......')
			return -1








	def changePasswd(self):
		#改密
		cardNum = input('请输入您要改密码的卡号，并以回车结束：')
		# 验证卡号是否存在
		cuser = self.allUser.get(cardNum)
		if cuser.card.cardID == 0:
			print('此卡已被销户，改密失败......')
			return -1
		if not cuser:
			print('该卡号不存在，改密失败>>>>>>')
			return -1
		# 验证是否锁定
		if cuser.card.cardLock:
			print('该卡已被锁定，请解锁后进行其他操作......')
			return -1

		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，该卡已被锁定，请解锁后进行其他操作>>>>>>')
			cuser.card.cardLock = True
			return -1
		newPasswd = input('请输入您的新密码：')
		newPasswdone = input('请再次输入：')
		if newPasswd != newPasswdone:
			print('两次输入密码不一致，改密失败.....')
			return -1
		cuser.card.cardPasswd = newPasswdone
		print('恭喜您改密成功!!请牢记您的新密码')



	def lockUser(self):
		#锁定
		cardNum = input('请输入您要锁定的卡号，并以回车结束：')
		# 验证账号
		cuser = self.allUser.get(cardNum)
		if cuser.card.cardID == 0:
			print('此卡已被销户，锁定失败......')
			return -1
		if not cuser:
			print('该卡号不存在，锁定失败>>>>>>')
			return -1
		if cuser.card.cardLock:
			print('该卡已被锁定!!!请解锁后进行其他操作......')
			return -1

		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，锁定失败>>>>>>')
			return -1

		# 验证身份证号
		tempIdCard = input('请输入身份证号：')
		if tempIdCard != cuser.idCard:
			print('身份证错误，锁定失败>>>>>>')
			return -1

		# 锁定
		cuser.card.cardLock = True
		print('锁定成功......')

	def unlockUser(self):
		#解锁
		cardNum = input('请输入您要解锁的卡号，并以回车结束：')
		# 验证账号
		cuser = self.allUser.get(cardNum)
		if cuser.card.cardID == 0:
			print('此卡已被销户，解锁失败......')
			return -1
		if not cuser:
			print('该卡号不存在，解锁失败>>>>>>')
			return -1

		if not cuser.card.cardLock:
			print('该卡未被锁定，无需解锁......')
			return -1


		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，解锁失败>>>>>>')
			return -1

		# 验证身份证号
		tempIdCard = input('请输入身份证号：')
		if tempIdCard != cuser.idCard:
			print('身份证错误，解锁失败>>>>>>')
			return -1

		# 锁定
		cuser.card.cardLock = False
		print('解锁成功......')

	def newCard(self):
		# 补卡
		cardNum = input('请输入您要补办的旧卡号，并以回车结束：')
		# 验证账号
		cuser = self.allUser.get(cardNum)
		if cuser.card.cardID == 0:
			print('此卡已被销户，补卡失败......')
			return -1
		if not cuser:
			print('该卡号不存在，锁定失败>>>>>>')
			return -1
		if cuser.card.cardLock:
			print('该卡已被锁定!!!请解锁后进行其他操作......')
			return -1

		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，锁定失败>>>>>>')
			return -1

		# 验证身份证号
		tempIdCard = input('请输入身份证号：')
		if tempIdCard != cuser.idCard:
			print('身份证错误，解锁失败>>>>>>')
			return -1


		cuser.card.cardID = self.randomCardId()
		print('恭喜您!!补卡成功，您的新卡号为：%s'%(cuser.card.cardID))

	def killUser(self):
		#销户
		cardNum = input('请输入您要销户卡号，并以回车结束：')
		# 验证账号
		cuser = self.allUser.get(cardNum)
		if cuser.card.cardID == 0:
			print('此卡已被销户，销户失败......')
			return -1
		if not cuser:
			print('该卡号不存在，销户失败>>>>>>')
			return -1
		if cuser.card.cardLock:
			print('该卡已被锁定!!!请解锁后进行其他操作......')
			return -1

		# 验证密码
		if not self.checkPasswd(cuser.card.cardPasswd):
			print('密码错误，销户失败>>>>>>')
			return -1

		# 验证身份证号
		tempIdCard = input('请输入身份证号：')
		if tempIdCard != cuser.idCard:
			print('身份证错误，销户失败>>>>>>')
			return -1
		judge = input('请问是否确认销户？回复：（yes/no）：')
		if judge == 'yes':
			cuser.card.cardID = 0
			print('销户成功!!')
		if judge == 'no':
			print('退出销户成功......')
			return -1




	def checkPasswd(self,realPasswd):
		for i in range(3):
			tempPasswd = input('请输入密码：')
			if tempPasswd == realPasswd:
				return True
		return False

	# 生成卡号
	def randomCardId(self):
		while True:
			str = ''
			for i in range(6):
				ch = chr(random.randrange(ord('0'), ord('9') + 1))
				str += ch

			#如果没有在字典中得到相同的字符串就返回none，可以以此为判据判断生成的随机数字是否重复
			if not self.allUser.get(str):
				return str


