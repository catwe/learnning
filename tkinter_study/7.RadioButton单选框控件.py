import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

def updata():
	print(r.get())


# tkinter内部变量的类型
r = tkinter.IntVar()

# 一组单选框要绑定同一变量
radiol = tkinter.Radiobutton(win,text='one',value=1,variable=r,command=updata)
radiol.pack()

radio2 = tkinter.Radiobutton(win,text='two',value=2,variable=r,command=updata)
radio2.pack()

radio3 = tkinter.Radiobutton(win,text='three',value=3,variable=r,command=updata)
radio3.pack()






win.mainloop()