import os #文件模块
# print(os.uname()) window不提供
print(os.name)  #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.environ.get('PATH'))#要获取某个环境变量的值，可以调用os.environ.get('key')：

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('F:/ali213_pk/Desktop/python','newfile')
# 然后创建一个目录:
# os.mkdir('F:/ali213_pk/Desktop/python/newfile')
# 删掉一个目录:
# os.rmdir('F:/ali213_pk/Desktop/python/newfile')

