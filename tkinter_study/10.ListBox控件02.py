import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
# win.geometry('400x400+500+20')


# EXTENDED可以使listbox支持shift和ctrl
lb = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)
lb.pack()
for x in ['好的','kuaile','那又怎样','test','delt','好的','kuaile','那又怎样',
          'test','delt','好的','kuaile','那又怎样','test','delt']:
	# 按顺序添加
	lb.insert(tkinter.END,x)

# 按住shirt可以实现连选
# 按住ctrl可以实现多选

# 加滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)

# 额外属性赋值
sc['command']= lb.yview

win.mainloop()