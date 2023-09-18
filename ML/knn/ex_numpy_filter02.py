import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps


def apply_filter(input_img, kernel):
    output_img = np.copy(input_img)
    for i in range(1, input_img.shape[0] - 1):
        for j in range(1, input_img.shape[1] - 1):
            output_img[i, j] = np.sum(input_img[i - 1:i + 2, j - 1:j + 2] * kernel, axis=(0, 1))
    return np.clip(output_img, 0, 1)


def load_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    original_img = Image.open(file_path)
    original_img.thumbnail((300, 300))  # Resize for display
    img_tk = ImageTk.PhotoImage(original_img)
    img_label.config(image=img_tk)
    img_label.original_img = original_img
    img_label.image = img_tk


def on_filter_selected(event):
    kernel_map = {
        "Unsharp": np.array([ [-1/6, -2/3, -1/6], [-2/3,  11/6, -2/3],  [-1/6, -2/3, -1/6]]), #이미지의 선명도를 향상시킵니다.
        "Box Blur": np.array([ [1/9, 1/9, 1/9], [1/9, 1/9, 1/9],  [1/9, 1/9, 1/9]]),  #이미지를 부드럽게 합니다.
        "Gaussian Blur": np.array([[1 / 16, 1 / 8, 1 / 16], [1 / 8, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 16]])
    }

    selected_filter = filter_combobox.get() #사용자가 선택한 값
    kernel = kernel_map[selected_filter]    #필터 가져오기

    original_np_img = np.array(img_label.original_img) / 255.0   #이미지 정규화:
    filtered_img = apply_filter(original_np_img, kernel) #필터 적용
    filtered_img = Image.fromarray((filtered_img * 255).astype(np.uint8))

    img_tk = ImageTk.PhotoImage(filtered_img)
    after_label.config(image=img_tk)
    after_label.image = img_tk


root = tk.Tk()
root.title("Image Filter App")

load_btn = tk.Button(root, text="Load Image", command=load_image)
load_btn.pack(pady=20)

img_label = tk.Label(root)
img_label.pack(padx=20, side=tk.LEFT)

after_label = tk.Label(root, text="After")
after_label.pack(padx=20, side=tk.RIGHT)

filter_label = tk.Label(root, text="Choose a Filter")
filter_label.pack(pady=10)

filter_combobox = ttk.Combobox(root, values=["Unsharp", "Box Blur", "Gaussian Blur"], state="readonly")
filter_combobox.bind("<<ComboboxSelected>>", on_filter_selected)
filter_combobox.pack(pady=10)

root.mainloop()