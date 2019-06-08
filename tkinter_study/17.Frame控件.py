import tkinter

# 主窗口
win = tkinter.Tk()
# 设置标题
win.title('王聪专用记事本')
# 设置大小和位置
win.geometry('400x400+500+20')


'''
框架控件
在屏幕显示一个矩形,作为一个容器使用

'''
frm = tkinter.Frame(win)
frm.pack()

# left
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l,text='左上',bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frm_l,text='左下',bg='blue').pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)


# Right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r,text='右上',bg='yellow').pack(side=tkinter.TOP)
tkinter.Label(frm_r,text='右下',bg='red').pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.LEFT)




win.mainloop()