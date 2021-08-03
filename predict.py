#
# -------------------------------------#
#       对单张图片进行预测
# -------------------------------------#
# from yolo import YOLO
# from PIL import Image

# yolo = YOLO()

# while True:
#     img = input('Input image filename:')
#     try:
#         image = Image.open(img)
#     except:
#         print('Open Error! Try again!')
#         continue
#     else:
#         r_image = yolo.detect_image(image)
#         r_image.show()
# 对多张图片进行检测

from yolo import YOLO
from PIL import Image
import os

yolo = YOLO()
filepath = "./val/images/"
filename = os.listdir(filepath)
while True:
    for i in filename:
        print(i)
        image = i.strip().split(".")
        j = i.split(".")[0]


        # img = input('Input image filename:')
        try:
            img = image[0] + ".jpg"
            imag = os.path.join(filepath, img)
            im = Image.open(imag)
            print(im)
        except:

            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(im)
            r_image.save('./val/result/' + j + '.jpg')

