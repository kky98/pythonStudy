from tkinter import *
from tkinter import messagebox
from lotto_file import fn_lotto as lotto
app = Tk()
lbl = Label(app, text='로또 수량')
lbl.grid(row=0, column=0)
txt = Entry(app)
txt.grid(row=0, column=1)
def fn_click():
    cnt = int(txt.get())
    makelotto = lotto(cnt)
    messagebox.showinfo("행운의 숫자", makelotto)
# 버튼 클릭 이벤트
btn = Button(app, text='ok', command=fn_click)
btn.grid(row=1, column=1)
app.mainloop() # 실행
