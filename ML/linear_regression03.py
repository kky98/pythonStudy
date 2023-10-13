import numpy as np
import matplotlib.pyplot as plt
# 다중선형회귀
# x1 :공부시간, x2 : 과외시간,  y:성적
x1 = [2, 4, 6, 8]
x2 = [0, 4, 2, 3]
y = [81, 93, 91, 97]

ax = plt.axes(projection='3d')
ax.set_xlabel('study')
ax.set_ylabel('private')
ax.set_zlabel('score')
ax.dist=11
ax.scatter(x1, x2, y)
plt.show()

x1_data = np.array(x1)
x2_data = np.array(x2)
y_data = np.array(y)
a1 = 0     #기울기 1
a2 = 0     #기울기 2
b = 0     #y절편
lr = 0.05 #학습률
epochs = 2001 # 학습데이터에 대해서 몇번 학습할지
for i in range(epochs):
    y_hat = a1 * x1_data + a2 * x2_data  + b
    error = y_data - y_hat #실제값과 예측값의 차이
    a1_diff = -(1/len(x1_data)) * sum(x1_data * error) #오차함수를 a로 미분
    a2_diff = -(1/len(x2_data)) * sum(x2_data * error)  # 오차함수를 a로 미분
    b_diff = -(1/len(x1_data)) * sum(y_data -y_hat)          #오차함수를 b로 미분
    a1 = a1 - lr * a1_diff #학습률을 곱하여 a 업데이트
    a2 = a2 - lr * a2_diff  # 학습률을 곱하여 a 업데이트
    b = b - lr * b_diff #학습률을 곱하여 b 업데이트
    if i % 100 == 0:
        print("epochs=%.f, 기울기1 a1=%.04f"
              ",기울기2 a2=%.04f, y절편=%.04f"%(i, a1, a2, b))
# pip install statsmodels

import statsmodels.api as statm
import statsmodels.formula.api as statfa
import pandas as pd
#from matplotlib.pyplot import figure
data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
X = [i[0:2] for i in data]
y = [i[2] for i in data]

X_1=statm.add_constant(X)
results=statm.OLS(y,X_1).fit()

hour_class=pd.DataFrame(X,columns=['study_hours','private_class'])
hour_class['Score']=pd.Series(y)

model = statfa.ols(formula='Score ~ study_hours + private_class', data=hour_class)

results_formula = model.fit()

a, b = np.meshgrid(np.linspace(hour_class.study_hours.min(),hour_class.study_hours.max(),100),
np.linspace(hour_class.private_class.min(),hour_class.private_class.max(),100))

X_ax = pd.DataFrame({'study_hours': a.ravel(), 'private_class': b.ravel()})
fittedY=results_formula.predict(exog=X_ax)

fig = plt.figure()
graph = fig.add_subplot(111, projection='3d')

graph.scatter(hour_class['study_hours'],hour_class['private_class'],hour_class['Score'],
c='blue',marker='o', alpha=1)
graph.plot_surface(a,b,fittedY.values.reshape(a.shape),
rstride=1, cstride=1, color='none', alpha=0.4)
graph.set_xlabel('study hours')
graph.set_ylabel('private class')
graph.set_zlabel('Score')
graph.dist = 11

plt.show()