import numpy as np
import matplotlib.pyplot as plt

# x :공부시간, y:성적
x = [2, 4, 6, 8]
y = [81, 93, 91, 97]
x_data = np.array(x)
y_data = np.array(y)
a = 0     #기울기
b = 0     #y절편
lr = 0.05 #학습률
epochs = 2001 # 학습데이터에 대해서 몇번 학습할지
for i in range(epochs):
    y_hat = a * x_data + b
    error = y_data - y_hat #실제값과 예측값의 차이
    a_diff = -(1/len(x_data)) * sum(x_data * error) #오차함수를 a로 미분
    b_diff = -(1/len(x_data)) * sum(error)          #오차함수를 b로 미분
    a = a - lr * a_diff #학습률을 곱하여 a 업데이트
    b = b - lr * b_diff #학습률을 곱하여 b 업데이트
    if i % 100 == 0:
        print("epochs=%.f, 기울기 a=%.04f, y절편=%.04f"%(i, a, b))

y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()
