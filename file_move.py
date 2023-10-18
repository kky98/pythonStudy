import os
import pandas as pd
import shutil
#원본 폴더 경로


dev_folder="./dev_back"
#경로를 읽어올 파일
excel_file = "path_file.xlsx"

#경로 읽어오기
df =pd.read_excel(excel_file)
for dir_path in df["path"]:
    filename =os.path.basename(dir_path)
    source_path =os.path.join(dev_folder,filename)
    print(dir_path)
    if not os.path.exists(source_path):
        print("경로에 파일 없음")
        continue
    folder = os.path.dirname(dir_path)
    print(folder)
    #해당 경로에 폴더 없음 생성
    if not os.path.exists(folder):
        os.makedirs(folder)
    shutil.move(source_path,dir_path)