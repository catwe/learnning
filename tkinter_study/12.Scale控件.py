import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')


'''
供用户通过拖动改变某些变量的值，可以水平，也可以竖直
tkinter.HORIZONTAL 水平
tkinter.VERTICAL   竖直
tickinterval      选择值将会为该值的倍数
length         水平为宽度，竖直为高度

'''

scale = tkinter.Scale(win,from_=0,to=100,orient=tkinter.VERTICAL,tickinterval=10,length=200)
scale.pack()

# 设置值
scale.set(25)


# 取值
def showNum():
	print(scale.get())

tkinter.Button(win,text='按钮',command=showNum).pack()




win.mainloop()