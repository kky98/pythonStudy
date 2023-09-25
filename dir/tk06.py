from tkinter import *
from tkinter import ttk
from inlotto import fn_lotto as lotto
import requests
from bs4 import BeautifulSoup
import os
import  urllib.request as req

app = Tk()
text = Text(app, wrap='word')
text.grid(row=0, column=0, columnspan=4, sticky='nsew')
scrollbar = ttk.Scrollbar(app, orient=VERTICAL, command=text.yview())
scrollbar.grid(row=1, column=0, columnspan=4, sticky='ns')
entry = Entry(app)
entry.grid(row=1, column=0, columnspan=4, sticky='ew')

def fn_get_img(req_url):
    #요정 url이미지 저장
    res =requests.get(req_url)
    print(res.status_code)
    # 응답 내용 파싱
    soup =BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())

    img_arr =soup.find_all('img')
    print(img_arr)
    # 폴더 생성
    if not os.path.exists('images'):
        os.mkdir('images')
    for i, img in enumerate(img_arr):
        img_src = img.get('src')
        print(img_src)
        if img_src:
            if img_src.startswith('http'):
                local_path = 'images/img_'+str(i)+'.jpg' #경로
                req.urlretrieve(img_src,local_path)
                text.insert(END,f"down {img_src} to {local_path}\n")

def append_text():
    url = entry.get()
    fn_get_img(url)
    text.insert(END,url+'\n')
    entry.delete(0,END)

def clear_text():
    text.delete(1.0, END)


def search_text():
    pass


s_btn = Button(app, text='입력', command=append_text)
s_btn.grid(row=2, column=0)
c_btn = Button(app, text='삭제', command=clear_text)
c_btn.grid(row=2, column=1)
q_btn = Button(app, text='검색', command=search_text)
q_btn.grid(row=2, column=2)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

app.mainloop()