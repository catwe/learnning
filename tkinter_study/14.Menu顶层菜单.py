import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

def func():
	print('点击成功！')


# 菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

# 创建一个菜单选项
menul = tkinter.Menu(menubar,tearoff=False)
# 给菜单选项添加内容
for item in ['PHP','C/C++','Python','Java','退出']:
	if item =='退出':
		menul.add_separator()
		menul.add_command(label=item,command=win.quit)
	else:
		menul.add_command(label=item,command=func)

# 向菜单条上添加内容
menubar.add_cascade(label='语言',menu=menul)


menu2 = tkinter.Menu(menubar,tearoff=False)
menu2.add_command(label='未来')
menu2.add_command(label='现在')
menu2.add_command(label='过去')
menubar.add_cascade(label='时间',menu=menu2)


win.mainloop()