import tkinter
from tkinter import ttk
# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')

tree = ttk.Treeview(win)
tree.pack()

# 添加一级树枝
treeF1 = tree.insert('',0,'中国',text='中国CH',values=('F1'))
treeF2 = tree.insert('',1,'美国',text='美国US',values=('F2'))
treeF3 = tree.insert('',2,'英国',text='英国ENC',values=('F3'))

# 添加二级树枝
tree1_1 = tree.insert(treeF1,0,'重庆',text='中国重庆',values=('F1_1'))
tree1_2 = tree.insert(treeF1,1,'广东',text='中国广东',values=('F1_2'))
tree1_3 = tree.insert(treeF1,2,'河南',text='中国河南',values=('F1_3'))


tree2_1 = tree.insert(treeF2,0,'德克萨斯州',text='美国德克萨斯州',values=('F2_1'))
tree2_2 = tree.insert(treeF2,1,'纽约',text='美国纽约',values=('F2_2'))
tree2_3 = tree.insert(treeF2,2,'旧金山',text='美国旧金山',values=('F2_3'))



win.mainloop()