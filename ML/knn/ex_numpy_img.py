import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('./a.JPG')[:, :, :3]
plt.imshow(img)
plt.show()
print(img)

def apply_filter(input_img, kernel):
    output_img = np.copy(input_img)
    for i in range(1, input_img.shape[0] - 1):
        for j in range(1, input_img.shape[1] - 1):
            output_img[i, j] = np.sum(input_img[i-1: i +2
                                      , j-1:j + 2]*kernel,axis=(0,1))
    return np.clip(output_img, 0, 1)
gaussian_blur = np.array([[1/16, 1/8, 1/16]
                        , [1/8, 1/4, 1/8]
                         ,[1/16, 1/8, 1/16]])
img_normalized = img / 255.0 # 0 ~1 정규화
output = apply_filter(img_normalized, gaussian_blur)
plt.imshow(output)
plt.show()
