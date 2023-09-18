import matplotlib.pyplot as plt
import numpy as np
# 유클리드 거리 점과 점의 거리
def euclidean(x, y):
    return np.sqrt(np.sum((x - y)**2))

a = np.array([1, 0])
b = np.array([0, 6])
print(euclidean(a, b))
plt.figure(figsize=(6, 6))
plt.scatter([a[0],b[0]], [a[1], b[1]])
plt.show()
