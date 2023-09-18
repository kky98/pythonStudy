import numpy as np

# 배열과 차이
arr = [1, 2, 3, 4]
print("arr:", arr)
print("arr type:", type(arr))

a = np.array(arr)
print("ndarry shape:", a.shape)
print("dtype :", a.dtype)
print("dim 차원:", a.ndim)
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("ndarry shape:", b.shape)
print("dtype :", b.dtype)
print("dim 차원:", b.ndim)
c = np.array([ [[1,2,3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] ])
print("ndarry shape:", c.shape)
print("dtype :", c.dtype)
print("dim 차원:", c.ndim)
d = np.array([[[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]]])
print("ndarry shape:", d.shape)
print("dtype :", d.dtype)
print("dim 차원:", d.ndim)
print(d)
data1 = np.array([[1, 2],[3, 4]])
data2 = np.array([[0, 1],[1, 0]])
print(data1)
print(data2)
# dot product
data3 = np.dot(data1, data2)
print(data3)
# 전치행렬
data4 = np.transpose(data3)
print(data4)
test = np.arange(10)
print(test)
print(test.shape, test.dtype, test.ndim)
# 형태 변경 reshape
print('2 x 5', test.reshape(2, 5))
print('5 x 2', test.reshape(5, 2))
print('1d', test.reshape(-1, 1))