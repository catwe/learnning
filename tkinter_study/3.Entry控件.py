import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

'''
输入控件
用于显示简单的文本内容

'''
# 绑定变量
e = tkinter.Variable()

#show='*' 以*的形式密文显示
entry = tkinter.Entry(win,textvariable=e)
entry.pack()
# e就代表输入框这个对象
e.set('请输入密码....')
# 取值
print(e.get())
print(entry.get())





win.mainloop()