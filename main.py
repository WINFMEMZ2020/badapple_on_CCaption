from cv2 import cv2
import numpy as np
import os
from colorama import Back,init

init(autoreset=False)

# 分割图片
filenames = os.listdir(r'D:\\output\\')
filenames.sort()
for picture in filenames:
    pic_path = "D://output//" + picture  # 分割的图片的位置
    pic_target = './done/' + picture + "/"  # 分割后的图片保存的文件夹
    if not os.path.exists(pic_target):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(pic_target)
    cut_width = 64
    cut_length = 64
    picture = cv2.imread(pic_path)
    (width, length, depth) = picture.shape
    print("width =" + str(width) + "，length=" + str(length))
    pic = np.zeros((cut_width, cut_length, depth))
    num_width = int(width / cut_width)
    num_length = int(length / cut_length)
    for i in range(0, num_width):
        for j in range(0, num_length):
            pic = picture[i * cut_width: (i + 1) * cut_width, j * cut_length: (j + 1) * cut_length, :]
            result_path = pic_target + '{}_{}.jpg'.format(i + 1, j + 1)
            cv2.imwrite(result_path, pic)
    print(Back.GREEN + "Done!" + pic_path,end="")
    print(Back.BLACK + "")
print("DONE!!!")
