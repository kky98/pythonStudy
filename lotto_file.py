import random
def fn_lotto(user_num):
    arr = []
    for i in range(user_num):
        lotto = set()
        while True:
            lotto.add(random.randint(1, 45)) # 랜덤 정수 1 ~ 45
            if len(lotto) == 6:
                break
        arr.append(lotto)
    print("good luck")
    return arr







if __name__ == '__main__':
    #해당 모듈에서 실행시
    my_lotto = fn_lotto(5)
    print(my_lotto)
else:
    print("import 했을때")

