import random
user_num = int(input("로또 생성기 입니다 ^^ 몇개를 원하세요?"))
for i in range(user_num):
    lotto = set()
    while True:
        lotto.add(random.randint(1, 45)) # 랜덤 정수 1 ~ 45
        if len(lotto) == 6:
            break
    print(lotto)
print("good luck")
a = input()