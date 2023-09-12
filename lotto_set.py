# 사용자가 로또 번호에 포함시키고 싶은 번호를 입력 받아
# 원하는 수량 만큼 로또 번호를 생성해 주세요 ^^
import random
def set_lotto(param):
    while True:
        param.add(random.randint(1, 45))  # 랜덤 정수 1 ~ 45
        if len(param) == 6:
            break
    return param
# param1 : 수량, param2: 0 ~ 6 개의 1 ~ 45 사이 수
while True:
    # 1.수량만 있을 경우
    # 2.희망 하는 숫자가 1 ~ 6개 경우
    # 3.희망 하는 숫자가 6개를 넘는 경우  -> 다시 입력 받기
    user = input("로또 수량과 희망하는 숫자를 띄어쓰기로 입력 해주세요(종료:q):").split()
    if len(user) == 1:
        cnt = int(user[0])
        for i in range(cnt):
            print(set_lotto(set()))
    elif len(user) < 8:
        flag = False
        for n in user:
            if int(n) < 1 or int(n) > 45:
                print('희망 숫자는 1 ~ 45 사이 숫자')
                flag = True
        if flag:
            continue
        cnt = int(user[0])
        for i in range(cnt):
            print(set_lotto(set(user[1:])))
    elif len(user) > 7:
        print('희망 숫자는 6개를 초과 하면 안됩니다.')
if __name__ == '__main__':
    print('행운의 로또생성기 ^^')