from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from PIL import  Image
model=load_model("./model/09--0.0613.hdf5")
model.summary()
#이미지 로드
image =Image.open("7.png")
#이미지 크기 변환
image =image.resize((28,28)).convert('L') # 흑백 28x28
# 이미지 흑백전환
#image=255-np.array(image)
#데이터 전처리
image_arr = np.array(image)
image_arr = image_arr.reshape(1,784).astype('float32')/255.0
pred =model.predict(image_arr)
print(np.argmax(pred))
