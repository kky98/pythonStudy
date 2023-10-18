import os
from keras.datasets import mnist
import numpy as np
from keras.utils import to_categorical
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

#매 실행마다 동일한 결과를 얻기 위해 시드 설정
seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)

mnist.load_data() # 로 데이터 불러오기
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#데이터의 크기 출력
print(f"학습 데이터 shape: {x_train.shape}")
print(f"테스트 데이터 shape: {x_test.shape}")

#이미지 출력
import matplotlib.pyplot as plt
#plt.imshow(x_train[0], cmap="Greys")

#데이터 준비
x_train_reshape = x_train.reshape(x_train.shape[0], 784).astype("float32") / 255
x_test_reshape = x_test.reshape(x_test.shape[0], 784).astype("float32") / 255
y_train_cate = to_categorical(y_train, 10)
y_test_cate = to_categorical(y_test, 10)

#모델 구조
model = Sequential()
model.add(Dense(512, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()

#모델 컴파일
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#모델 저장 폴더
path = "./model/"
if not os.path.exists(path):
    os.mkdir(path)
file_name = path + "{epoch:02d}--{val_loss:.4f}.hdf5"
checkpoint =ModelCheckpoint(filepath=file_name,monitor='val_loss',verbose=1, save_best_only=True)
early_stopping =EarlyStopping(monitor='val_loss',patience=10)
history =model.fit(x_train_reshape,y_train_cate,epochs=100,batch_size=200,validation_data=(x_test_reshape,y_test_cate),callbacks=[early_stopping,checkpoint])
#모델 학습
model.fit(x_train_reshape, y_train_cate, epochs=10)

#학습 및 테스트 정확도 출력
train_accuracy = model.evaluate(x_train_reshape, y_train_cate)[1]
test_accuracy = model.evaluate(x_test_reshape, y_test_cate)[1]
print(f'학습 acc: {train_accuracy}')
print(f'테스트 acc: {test_accuracy}')
v_loss=history.history['val_loss']
loss=history.history['loss']
#그래프로
import matplotlib.pyplot as plt
cnt = np.arange((len(v_loss)))
plt.plot(cnt, v_loss, marker='.',c='red',label='test_loss')
plt.plot(cnt, loss, marker='.',c='blue',label='train_loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

#예측 출력
predictions = model.predict(x_test_reshape)
print(f'첫 번째 테스트 이미지의 예측 결과: {predictions[0]}')