from tkinter import *
from tkinter import ttk
from lotto_file import fn_lotto as lotto

app = Tk()
text = Text(app, wrap='word')
text.grid(row=0, column=0, columnspan=4, sticky='nsew')
scrollbar = ttk.Scrollbar(app, orient=VERTICAL, command=text.yview())
scrollbar.grid(row=0, column=4, sticky='ns')
entry = Entry(app)
entry.grid(row=1, column=0, columnspan=4, sticky='ew')
def append_text():
    cnt = int(entry.get())
    set_arr = lotto(cnt)
    for i in list(set_arr):
        # text.insert(END, entry.get() + '\n')
        text.insert(END, str(i) + '\n')
    entry.delete(0,'end')
    text.see(END)
def clear_text():
    text.delete(1.0, END)
def search_text():
    pass
s_btn = Button(app, text='입력', command=append_text)
s_btn.grid(row=2, column=0)
c_btn = Button(app, text='내용 삭제', command=clear_text)
c_btn.grid(row=2, column=1)
q_btn = Button(app, text='검색', command=search_text)
q_btn.grid(row=2, column=2)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.mainloop()
