from tkinter import *
from tkinter import ttk
from inlotto import fn_lotto as lotto
app=Tk()
text =Text(app,wrap='word')
text.grid(row=0,column=0,columnspan=4,sticky='nsew')
scrollbar =ttk.Scrollbar(app,orient=VERTICAL,command=text.yview())
entry =Entry(app)
entry.grid(row=1,column=0,columnspan=4,sticky='ew')
def append_text():
    cnt = int(entry.get())
    rlotto=list(lotto(cnt))
    print(rlotto,type(rlotto))

    for i in rlotto:
        text.insert(END, str(rlotto) + '\n')

    entry.delete(0, 'end')
    text.see(END)
def clear_text():
    text.delete(1.0,END)
def search_text():
    pass

s_btn =Button(app,text='입력',command=append_text)
s_btn.grid(row=2,column=0)
c_btn =Button(app,text='삭제',command=clear_text)
c_btn.grid(row=2,column=1)
q_btn =Button(app,text='검색',command=search_text)
q_btn.grid(row=2,column=2)
app.grid_rowconfigure(0,weight=1)
app.grid_columnconfigure(0,weight=1)

app.mainloop()