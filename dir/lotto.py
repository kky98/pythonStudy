import random

user_num =int(input("몇개"))
for i in range(user_num):
    lotto = set()
    while True:
        lotto.add(random.randint(1,45))
        if len(lotto) == 6 :
            break
    print(lotto)