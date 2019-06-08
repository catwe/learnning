import cv2 as cv
import numpy as np

# 图片的分辨率为200*300，这里b, g, r设为随机值，注意dtype属性
# b = np.random.randint(0, 255, (300, 300), dtype=np.uint8)
# g = np.random.randint(0, 255, (300, 300), dtype=np.uint8)
# r = np.random.randint(0, 255, (300, 300), dtype=np.uint8)

# 合并通道，形成图片
# img = cv2.merge([b, g, r])

# 读取图片
img = cv.imread('test.jpg')
# 显示图片
cv.imshow('test', img)
cv.waitKey(0)
cv.destroyWindow('test')
