import time
class Admin(object):
	admin = '1'
	passwd = '1'

	def printAdminView(self):
		print('*********************************************************************************')
		print('*                                                                               *')
		print('*                                                                               *')
		print('*                                                                               *')
		print('*                            欢迎登陆十八画生银行                               *')
		print('*                          版权：十八画生 by Mr.Wang                            *')
		print('*                                                                               *')
		print('*                                                       注册资本：10亿元        *')
		print('*                                                       创建日期：2019/4/12     *')
		print('*********************************************************************************')

	def sysFunctionView(self):
		print('*************************************************************************************')
		print('*   开户 (0 open)                                    查询（1 find）                 *')
		print('*   取款（2 Withdraw）                               存款（3 deposit）              *')
		print('*   转账（4 Transfer）                               改密（5 Change password）      *')
		print('*   锁定（6 lock）                                   解锁（7 unlock）               *')
		print('*   补卡（8 Patch card）                             销户（9 eliminat)              *')
		print('*                              退出（00 quit）                                      *')
		print('*************************************************************************************')
	#退出
	def adminLogin(self):
		inputAdmin = input('请输入管理员账号：')
		if self.admin != inputAdmin:
			print('***************账号输入错误***************')
			time.sleep(3)
			return -1
		inputPasswd = input('请输入管理员密码：')
		if self.passwd != inputPasswd:
			print('***************密码错误*****************')
			time.sleep(3)
			return -1
		# 程序执行到这里说明账号密码正确
		else:
			print('登陆成功，请稍后......')
			time.sleep(2)
			return 0
	def adminOption(self):
		inputAdmin = input('请输入管理员账号：')
		if self.admin != inputAdmin:
			print('***************账号输入错误***************')
			return -1
		inputPasswd = input('请输入管理员密码：')
		if self.passwd != inputPasswd:
			print('***************密码错误*****************')
			return -1
		# 程序执行到这里说明账号密码正确
		else:
			print('操作成功，请稍后......')
			time.sleep(2)
			return 0
