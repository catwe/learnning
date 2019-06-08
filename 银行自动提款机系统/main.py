'''
人
类名：User
属性：姓名  身份证号 电话 卡
行为：


提款机
类名：ATM
属性：
行为：开户  ， 查询 ， 取款 ， 销户 ， 锁定 ， 改密 ，解锁 ， 转账 ，补卡


卡
类名：Card
属性：卡号 密码 余额
行为：



银行
类名：Bank
属性：用户列表 提款机


界面
类名：Admin
属性：
行为：管理员界面 管理员登陆 管理员验证 用户界面

'''

from admin import Admin
from atm import ATM
import time
import pickle
import os

def main():
	#界面对象
	view = Admin()

	# 管理员开机
	view.printAdminView()
	if view.adminLogin():
		return -1

	# 提款机对象+文件操作
	filepath = os.path.join(os.getcwd(), 'allUsers.txt')
	# f = open(filepath, 'rb')
	allUsers = {}
	scores = {}  # scores is an empty dict already
	if os.path.getsize(filepath) > 0:
		with open(filepath, "rb") as f:
			unpickler = pickle.Unpickler(f)
			allUsers = unpickler.load()

	atm = ATM(allUsers)

	while True:
		view.sysFunctionView()
		# 等待用户操作
		option = input('请输入操作数字：')
		if option == '0':
			#开户
			print('开户中......')
			atm.createUser()

			# 开户成功就存入账号
			filepath = os.path.join(os.getcwd(), 'allUsers.txt')
			f = open(filepath, "wb")
			pickle.dump(atm.allUser, f)
			f.close()

			time.sleep(3)
		elif option == '1':
			# 查询
			atm.searchUserInfo()
			time.sleep(3)
		elif option == '2':
			# 取款
			atm.getMoney()
			time.sleep(3)
		elif option == '3':
			# 存款
			atm.saveMoney()
			time.sleep(3)
		elif option == '4':
			# 转账
			atm.tansferMoney()
			time.sleep(3)
		elif option == '5':
			# 改密
			atm.changePasswd()

			filepath = os.path.join(os.getcwd(), 'allUsers.txt')
			f = open(filepath, "wb")
			pickle.dump(atm.allUser, f)
			f.close()

			time.sleep(3)
		elif option == '6':
			# 锁定
			atm.lockUser()
			time.sleep(3)
		elif option == '7':
			# 解锁
			atm.unlockUser()
			time.sleep(3)
		elif option == '8':
			# 补卡
			atm.newCard()

			#存进去
			filepath = os.path.join(os.getcwd(), 'allUsers.txt')
			f = open(filepath, "wb")
			pickle.dump(atm.allUser, f)
			f.close()

			time.sleep(3)
		elif option == '9':
			# 销户
			atm.killUser()
			time.sleep(3)
		elif option == '00':
			# 退出
			if not view.adminOption():
				filepath = os.path.join(os.getcwd(),'allUsers.txt')
				f = open(filepath, "wb")
				pickle.dump(atm.allUser,f)
				f.close()
				return -1



if __name__ == '__main__':
	main()
