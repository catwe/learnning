import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

def updata():
	message = ''
	if hobby1.get() == True:
		message += '金钱\n'
	if hobby2.get() == True:
		message += '时间\n'
	if hobby3.get() == True:
		message += '美女\n'

	# 清楚text中所有的内容
	text.delete(0.0,tkinter.END)
	text.insert(tkinter.INSERT,message)


hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win,text='金钱',variable=hobby1,command=updata)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win,text='时间',variable=hobby2,command=updata)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win,text='美女',variable=hobby3,command=updata)
check3.pack()


text = tkinter.Text(win,width=50,height=10)
text.pack()




win.mainloop()