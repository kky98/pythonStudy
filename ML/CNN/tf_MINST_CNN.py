import os
from keras.datasets import mnist
import numpy as np
from keras.layers import MaxPooling2D
from keras.utils import to_categorical
import tensorflow as tf

from keras.layers import Dense,Flatten ,Conv2D

from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import Sequential
import matplotlib.pyplot as plt
#매 실행마다 동일한 결과를 얻기 위해 시드 설정
seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)

mnist.load_data() # 로 데이터 불러오기
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#데이터의 크기 출력
print(f"학습 데이터 shape: {x_train.shape}")
print(f"테스트 데이터 shape: {x_test.shape}")

x_train_reshape =x_train.reshape(x_train.shape[0],28,28,1).astype('float32')/255
x_test_reshape =x_test.reshape(x_test.shape[0],28,28,1).astype('float32')/255
y_train_cate=to_categorical(y_train)
y_test_cate=to_categorical(y_test)

model = Sequential()
model.add(Conv2D(32,kernel_size=(3,3),input_shape=(28,28,1),activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['acc'])
#모델 저장 폴더
path = "./model_cnn/"
if not os.path.exists(path):
    os.mkdir(path)
file_name = path + "{epoch:02d}--{val_loss:.4f}.hdf5"
checkpoint =ModelCheckpoint(filepath=file_name,monitor='val_loss',verbose=1, save_best_only=True)
early_stopping =EarlyStopping(monitor='val_loss',patience=10)
history =model.fit(x_train_reshape,y_train_cate,validation_data=(x_test_reshape,y_test_cate),epochs=30,batch_size=100,verbose=0,callbacks=[early_stopping,checkpoint])
v_loss =history.history['val_loss']
loss=history.history['loss']
cnt=np.arange(len(v_loss))
#그래프
plt.plot(cnt,v_loss,marker='.',c='red',label='test_loss')
plt.plot(cnt,loss,marker='.',c='blue',label='train_loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()