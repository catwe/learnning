import cv2 as cv
import numpy as np


# 读取图片
img = cv.imread('test.jpg')
# 显示图片
cv.imshow('test', img)

# 参数1：图像
# 参数2：滤波器大小
# 参数3：标准差
gaosi = cv.GaussianBlur(img,(3,3),0) #模糊图像
cv.imshow('gaosi',gaosi)

# 中值滤波函数
# 参数1：图像
# 参数2：滤波尺寸
middle = cv.medianBlur(img,5) # 填充白色噪点
cv.imshow('zhongzhi',middle)
cv.waitKey(0)
cv.destroyWindow('test')
