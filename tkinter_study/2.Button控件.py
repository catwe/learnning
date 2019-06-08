
import tkinter

def func():
	print('欢迎登陆')

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

# 创建按钮
button1 = tkinter.Button(win,text='开始',command=func,width=5,height=2)
# 显示
button1.pack()

button2 = tkinter.Button(win,text='退出',command=win.quit)
# 显示
button2.pack()







win.mainloop()