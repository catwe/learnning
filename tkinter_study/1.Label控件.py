import tkinter

win = tkinter.Tk()
win.title('王聪专用记事本')
win.geometry('400x400+500+20')

# text:文本
# bg：背景色
# fg:字体颜色
#wraplength:指定text文本多宽进行换行
#justify:设置换行后的对齐方式
# anchor:位置 s南 n北 w西 e东 center中心 n, ne, e, se, s, sw, w, nw, or center
lable = tkinter.Label(win,
                      text='好',
                      bg='white',
                      fg='black',
                      font=('黑体',20),
                      width=10,
                      height=20,
                      wraplength=50,
                      justify='left',
                      anchor='se'
                      )

# 显示出来
lable.pack()






win.mainloop()