#-*- encoding: utf-8 -*-
import os
dir = os.getcwd()#해당 파일 경로
print(dir)
file_list = os.listdir(dir)
print(file_list)
#os.remove('C:\dev\pythonProject\test')#파일삭제
for v in file_list:
    # print(dir + "\\" + v)
    file = dir + "\\" +v
    if os.path.isfile(file):
        print(file, '파일 입니다.')
    elif os.path.isdir(file):
        print(file, '폴더 입니다.')
root = "C:\\dev\\pythonProject\\"
for dirpath, dirname, filename in os.walk(root):
    print(dirpath, dirname, filename)