import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

lbv = tkinter.StringVar()
# 与BROWSE相似，但是不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()
for x in ['好的','kuaile','那又怎样','test','delt']:
	# 按顺序添加
	lb.insert(tkinter.END,x)

# 打印当前列表中的选项
print(lbv.get())

# 设置选项
# lbv.set(('1','2','3'))

# 绑定事件
def myPrint(event):
	print(lb.get(lb.curselection()))

lb.bind('<Double-Button-1>', myPrint)




win.mainloop()