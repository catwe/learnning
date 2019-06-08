f  = open('F:/ali213_pk/Desktop/python/io.txt','r',encoding='gbk',errors='ignore')#读文件
print(f.read())#打印文件内容
f.close() #必须写 否则占用资源
with open('F:/ali213_pk/Desktop/python/io.txt','w') as x:   #使用with语句就不需要关闭文件了
	x.write('你好')
	# x.close()  多余
with open('F:/ali213_pk/Desktop/python/io.txt','r') as d:
	print(d.read())
with open('F:/ali213_pk/Desktop/python/io.txt','a') as k:    #不会覆盖原文本内容
	k.write('我是附加的')
with open('F:/ali213_pk/Desktop/python/io.txt','r') as l:
	print(l.read())