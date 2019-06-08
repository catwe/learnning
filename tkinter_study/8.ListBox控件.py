import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')


'''
列表框控件,可以包含一个或者多个文本框
作用:在listbox控件中显示一个字符串
'''

# 创建一个listbox，添加几个元素
lb = tkinter.Listbox(win,selectmode=tkinter.BROWSE)
lb.pack()
for x in ['好的','kuaile','那又怎样','test','delt']:
	# 按顺序添加
	lb.insert(tkinter.END,x)

# 在开始添加
lb.insert(tkinter.ACTIVE,'我是被添加在最前面的元素')


# 删除，参数1为删除开始的索引，参数2为结束索引，如果不指定参数2，只删除第一个索引出的内容
# lb.delete(1,3)
lb.delete(1)

# 选中 跟删除规则类似
lb.select_set(2,3)
# lb.select_set(2)

# 取消选中
lb.select_clear(2)

# 获取列表中元素的个数
print(lb.size())

# 从列表中取值
print(lb.get(2,4))

# 打印出当前的索引项
print(lb.curselection())

# 判断是否选中
print(lb.select_includes(2))

win.mainloop()