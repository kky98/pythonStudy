from keras.models import load_model
from keras.datasets import mnist
(x_train , y_train),(x_test , y_test) = mnist.load_data()
x_test_sample=x_test[0].reshape(1,784).astype("float32")/255
print(x_test_sample[0])
model=load_model("./model/09--0.0613.hdf5")
model.summary()
pred=model.predict(x_test_sample)
print(pred)

import numpy as np
pred_class=np.argmax(pred,axis=1)
print(pred_class)
import matplotlib.pyplot as plt
plt.imshow(x_test[0],cmap='Greys')
plt.show()