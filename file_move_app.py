from tkinter import ttk, filedialog, messagebox
import tkinter as tk
import os
import pandas as pd
import shutil

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("execel","*.xlsx;.xls")])
    if not filepath:
        return
    global df
    df = pd.read_excel(filepath)
    list_box.delete(0, tk.END)
    for idx, row in df.iterrows():
        list_box.insert(tk.END, row['path'])
def start_moving():
    global df
    if df is None:
        messagebox.showerror()
        return
    dev_folder = "./dev_back"
    for dir_path in df["path"]:
        filename = os.path.basename(dir_path)
        source_path = os.path.join(dev_folder, filename)
        print(dir_path)
        if not os.path.exists(source_path):
            print("경로에 파일 없음")
            continue
        folder = os.path.dirname(dir_path)
        print(folder)
        # 해당 경로에 폴더 없음 생성
        if not os.path.exists(folder):
            os.makedirs(folder)
        shutil.move(source_path, dir_path)
    messagebox.showinfo("Info","completed!")
app= tk.Tk()
app.title("file mover")
frame =ttk.Frame(app,padding="10")
frame.grid(row=0,column=0,sticky=(tk.W,tk.E,tk.N,tk.S))
load_btn =ttk.Button(frame,text="load excel",command=load_file)
load_btn.grid(row=0,column=0, sticky=tk.W , pady=5)
list_box=tk.Listbox(frame,width=50,height=15)
list_box.grid(row=1,column=0,pady=5)
start_btn=ttk.Button(frame,text='start',command=load_file)
start_btn.grid(row=2 , column=0 ,pady=5)
df=None
app.mainloop()