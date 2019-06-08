import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

def showInfo():
	print(entry.get())

entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win,text='打印',command=showInfo)
# 显示
button.pack()







win.mainloop()