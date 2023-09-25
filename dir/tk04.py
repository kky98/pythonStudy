from tkinter import *

def create_ball(canvas):
    x0,y0=100,150
    x1,y1=150,200
    canvas.create_oval(x0,y0,x1,y1,fill='red',tag='redBall')

def move_left(event):
    print("좌이동")
    canvas.move('redBall',-x_size,0)
    canvas.after(20)
    canvas.update()
def move_right(event):
    print("우")
    canvas.move('redBall',x_size,0)
    canvas.after(20)
    canvas.update()
def move_up(event):
    print('상')
    canvas.move('redBall',0,-y_size)
    canvas.after(20)
    canvas.update()
def move_down(event):
    print('하')
    canvas.move('redBall',0,y_size)
    canvas.after(20)
    canvas.update()
app=Tk()
canvas=Canvas(app,width=400,height=300)
canvas.pack()
x_size=2
y_size=2
create_ball(canvas)
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.bind('<Up>', move_up)
canvas.bind('<Down>', move_down)

canvas.focus_set()
canvas.pack()
app.mainloop()