# import selenium
#
# # 주석 영역 ^^
# num = 10
# float_num = 10.6
# str_msg = 'Hello, Nick'
# bool_type = True    # 변수 단어별 연결은 _ <- 사용 스네이크 표기법
# print(num, type(num))
# print(float_num, type(float_num))
# print(str_msg, type(str_msg))
# print(bool_type, type(bool_type))
# num = "hi"
# print(num)
# # 문자열은 '' or "" 으로 작성하면 공백 포함 또는 긴 문자열은
# # ''' ''' or """ """ 으로 작성
# msg = """
#       안녕 오늘은 수요일 ^^
#       주말 까지 2일 밖에 없어서 아쉽다....
# """
# print(msg)
# print('-' * 100)
# print(msg.replace("수요일", "목요일"))
# arr = msg.split('^^') # 문자 자르기 default 공백1
# print(arr)
#
# user_msg = int(input("숫자를 입력 하세요:"))
# print(str(user_msg))
# user_msg = input("단어를 띄어서 입력 하세요:").split()
# print(type(user_msg), user_msg)


# 동적배열 (Dynamic Array)
# [] <-- 비어 있는 배열
arr1 = [1, True, "hi", [2, 3,['nick']]]
print(arr1[1])  # index 1번 value
print(arr1[3][1])  # index 3번에 1번 value
# python 에서는 배열 곱하기가 가능
print(arr1 * 10)
print(arr1[3][2][0])
print(arr1[-1]) # 배열의 마지막 요소에 접근
# 슬라이스
print(arr1[1:3]) # 1인덱스 부터 3인덱스 -1 까지
print(arr1[:2])  # 처음부터 2 -1 까지
print(arr1[2:])  # 2인덱스 부터 끝까지
tuple_arr = tuple(arr1) # 튜플로 형변환 가능
print(tuple_arr, type(tuple_arr))
# set 중복을 허용하지 않는 자료구조
# {} 로 표현하지만 비어있는 set을 만들때는 set()으로 해야함
# {}<- 비어있는 중괄호는 dict 딕셔너리 타입을 의미함
set_data = set()
print(type(set_data))
set_data.add(1)
set_data.add(1) # 동일 값은 기존값 유지
print(set_data, '길이:', len(set_data))

import random
lotto = set()
while True:
    lotto.add(random.randint(1, 45)) # 랜덤 정수 1 ~ 45
    if len(lotto) == 6:
        break
print(lotto)
