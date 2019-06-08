import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')


'''
数值范围控件
'''
def updata():
	print(v.get())

# 绑定变量

v = tkinter.StringVar()

# incriment步长，默认为1
# values不要与from_=0,to=100,increment=1,同时使用
# value=(0,2,4,6,8)

# command只要改变值就会执行相应的方法
spinbox = tkinter.Spinbox(win,from_=0,to=100,increment=1,textvariable=v,command=updata)
spinbox.pack()

# 赋值
v.set(25)
# 取值
print(v.get())



win.mainloop()