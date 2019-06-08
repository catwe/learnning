import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')


# 创建菜单条
menubar = tkinter.Menu(win)

# 创建一个菜单选项
menu = tkinter.Menu(menubar,tearoff=False)

# 给菜单选项添加内容
for item in ['PHP','C/C++','Python','Java','退出']:
	menu.add_command(label=item)

menubar.add_cascade(label='语言',menu=menu)

def showMenu(event):
	menubar.post(event.x_root,event.y_root)
win.bind('<Button-3>',showMenu)

win.mainloop()