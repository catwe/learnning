import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
# win.geometry('400x400+500+20')

'''
文本控件
能显示多行文本
大量文本
'''
scroll = tkinter.Scrollbar()
# hight:显示行数
text = tkinter.Text(win,width=30,height=20)
#side:放到窗体的哪一侧
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = '''It's the answer told by lines that stretched around schools and churches in numbers this nation has never seen; by people who waited three hours and four hours, many for the very first time in their lives, because they believed that this time must be different; that their voice could be that difference.'''

# 插入内容
text.insert(tkinter.INSERT,str)








win.mainloop()