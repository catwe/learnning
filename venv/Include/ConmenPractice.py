#!/usr/bin/env python3
#!/-*coding:utf8*-/
'a test model'
__author__='WangCong'

import sys
def test():
	args = sys.argv
	if len(args)==1:
		print('Hello word!')
	elif len(args)==2:
		print('Hello %s!'%args[1])
	else:
		print('Too much')
if __name__=='__main__':
	print(test())


