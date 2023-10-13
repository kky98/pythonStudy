import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# scikit-learn 머신러닝 라이브러리
# pip install scikit-learn
from sklearn.linear_model import LinearRegression
model = LinearRegression()
df = pd.read_csv("./datasets/heights.csv")
# x :키, y:무게
x = df['height']
y = df['weight']
model.fit(x.values.reshape(-1, 1), y)
print(model.coef_)      # 기울기
print(model.intercept_) # y절편
plt.plot(x, y, 'o')
plt.plot(x, model.predict(x.values.reshape(-1, 1)))
plt.show()
print('test:', model.predict([[70]]))
