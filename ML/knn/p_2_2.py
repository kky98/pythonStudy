# -*- coding: utf-8 -*-
"""2-2. 데이터 전처리
## 생선 분류 문제
### 도미 데이터 준비하기
"""
#  bream 도미 25.4 cm, 242 g
import matplotlib.pyplot as plt
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
"""### 빙어 데이터 준비하기"""
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
length = bream_length + smelt_length
weight = bream_weight + smelt_weight
import numpy as np
# column_stack 각각의 1-d 배열을 입력으로 받아 각 배열은 하나의 열로 가지는 2d반환
print(np.column_stack(([1,2,3], [4,5,6])))
fish_data = np.column_stack((length, weight))
print(fish_data)
print(np.ones(5))
print(np.zeros(5))
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(fish_data
                                       ,fish_target,random_state=1)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
print(knn.score(x_test, y_test))
print(knn.predict([[25, 150]]))
import matplotlib.pyplot as plt
# plt.scatter(x_train[:,0], x_train[:,1])
# plt.scatter(25, 150, marker='^')

distances, indexes = knn.kneighbors([[25, 150]])
# plt.scatter(x_train[indexes, 0], x_train[indexes, 1], marker='D')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()
#
mean = np.mean(x_train, axis=0) #axis 축 0은 세로(행방향)
std = np.std(x_train, axis=0)   #편차
print(mean, std)

x_train_scaled = (x_train - mean) / std

new = ([25, 150] - mean) / std
plt.xlim((0, 1000))

plt.scatter(x_train[:,0], x_train[:,1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')

plt.scatter(x_train_scaled[:,0], x_train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

knn.fit(x_train_scaled, y_train)
print(knn.predict([new]))





