import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')


# 创建一个listbox，添加几个元素,支持多选功能
lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
lb.pack()
for x in ['好的','kuaile','那又怎样','test','delt']:
	# 按顺序添加
	lb.insert(tkinter.END,x)






win.mainloop()