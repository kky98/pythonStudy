import os
from PIL import Image
img_dir ="./dataset/"
keyword =["돌고래","향유고래","고래상어","쿠로미","헬로키티","한교동"]
for dir in keyword:
    main_path =img_dir + dir
    arr =os.listdir(img_dir+dir)
    print(arr)
    for file in arr:
        with Image.open(main_path+"/"+file) as img:
            width,hight =img.size

        print(img.width,img.height)
        if img.width<100 or img.height<100:
            os.remove(main_path+"/"+file)