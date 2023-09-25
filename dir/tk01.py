from tkinter import *
from tkinter import messagebox

app =Tk()

lbl=Label(app,text='이름')
lbl.grid(row=0,column=0)
txt = Entry(app)
txt.grid(row=0,column=1)

def fn_click():
    name=txt.get()
    messagebox.showinfo("이름",name)
btn =Button(app,text='ok',command=fn_click)
btn.grid(row=1,column=1)
app.mainloop()