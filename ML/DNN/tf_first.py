import tensorflow as tf
import numpy as np

print(tf.__version__)

data =np.loadtxt('../datasets/ThoraricSurgery.csv',delimiter=',')
#독립변수: 환자의 기록 종속변수: 수술후 사망0, 생존1

x=data[:,0:17]#모든행17개열
y= data[:,17]#모든행 마지막열

#딥러닝 구조설계
from keras.models import Sequential
from keras.layers import Dense
# 모델 틀
model =Sequential()
#히든레이어 추가
model.add(Dense(30,input_dim=17,activation='relu'))
#출력층
model.add(Dense(1,activation='sigmoid')) # 이항분류
model.summary() # 만들 모델의 구조 출력
#손실함수와 최적화방법 정의
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['acc'])
#학습 (30번) /batch_size=>10개 데이터씩
model.fit(x,y,epochs=30,batch_size=10)
#결과 출력
print(f"acc:{model.evaluate(x,y)[1]}")

