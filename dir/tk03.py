from tkinter import *

app =Tk()

def fn_click(event):
    print('마우스 클릭 위치',event.x,event.y)

def fn_push(event):
    print("키보드 문자",event.char)

frame= Frame(app,width=300,height=300)

#클릭
frame.bind("<Button-1>",fn_click)
frame.bind("<Key>",fn_push)
frame.focus_set()
frame.pack()
app.mainloop()