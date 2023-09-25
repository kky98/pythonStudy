import random

def fn_lotto(user_num):
    arr = []
    for i in range(user_num):
        lotto = set()
        while True:
         lotto.add(random.randint(1, 45))
         if len(lotto) ==6:
            break
        arr.append(lotto)
    print(arr)
    return  arr

if __name__ == '__main__':  #해당 모듈에서 실행시
    my_lotto = fn_lotto(3)
    print(my_lotto)
else:
    print("import 했을때")
# 사용자가 로또 번호에 포함시키고 싶은 번호를 입력받아 원하는 수량만큼 로또번호 생성하기
# param1 : 수량, param2: 가변형 0~6 개의 1~45 사이수
user = input("원하는 로또 수량과 희망하는 숫자를 띄어쓰기로 입력하세요").split()
last = int(user.pop(0))
print(last)
print(user)

all_arr = []

for k in range(last):

    for i in range():
        a = random.randint(1,45)
        arr.append(a)
    all_arr.append(arr)
print(all_arr)