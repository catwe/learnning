import tkinter
from tkinter import ttk

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

cv = tkinter.StringVar()
com = ttk.Combobox(win,textvariable=cv)
com.pack()

# 设置下拉数据
com['value'] = ('数学','英语','语文')

# 设置默认值
com.current(0)

# 绑定事件
def func(event):
	print(com.get())
	print(cv.get())
	print('kkkkk')
com.bind('<<ComboboxSelected>>',func)





win.mainloop()