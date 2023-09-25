# 주석
import pandas
import selenium
import numpy
num  = 10
float_num = 10.6
str_msg = '"Hello"'
bool_type = True
print(num, type(num))
print(float_num,type(float_num))
print(str_msg,type(str_msg))
print(bool_type,type(bool_type))

num= "hi"
print(num)
a = int(input("입력하시오"))
print(a,type(a))
a=a*a
print(a)

msg='''
ab8c
8
anc8
a8cnc
'''
print("------------------")
print(msg.replace("abc","aaa"))
arr =msg.split('8')
print(arr)
msg=input("단어").split()
print(msg)

# 동적배열
# []<----비어있는배열
print("-"*10)
arr1= [1,True,"h1",[2,3]]
print(arr1[1])
print(arr1[3][1])
arr2=arr1*10
print(arr2[-1])
# 슬라이스
print(arr1[1:3]) #1부터 3전까지
print(arr1[:3])#0번째부터 숫자-1 까지
print(arr1[2:])#숫자부터 마지막

tuple_arr=tuple(arr1)
print(tuple_arr,type(tuple_arr))
tuple_arr=list(tuple_arr)
print(tuple_arr,type(tuple_arr))

#set 중복을 허용하지 않는 자료구조
#{}로 표현하지만 비어있는 set을 만들때는 set()으로 선언
#{}비어있는 중괄호는 dict 딕셔너리 타입 의미
set_data =set()
print(type(set_data))
set_data.add(1)
set_data.add(1)
print(set_data,"길이",len(set_data))

import random
lotto =set()

while True:
    lotto.add(random.randint(1,45))
    if len(lotto) == 6 :
        break
print(lotto)