import cv2 as cv
import numpy as np


def access_pixel(image):
	"""访问图像所有的像素"""
	print(image.shape)

	# 获取图像的高度，图像的高度为shape的第一个值（维度）
	height = image.shape[0]
	# 获取图像的宽读，图像的宽度为shape的第二个值（维度）
	width = image.shape[1]
	# 获取图像通道数目，图像的通道数目为shape的第三个值（维度）
	# 加载进来的图像都有三个通道，三个通道是图像的RGB
	channels = image.shape[2]
	print("width: %s,height: %s channels: %s" % (width, height, channels))

	# 循环获取每个像素点，并且修改，然后存储修改后的像素点
	for row in range(height):
		for col in range(width):
			for c in range(channels):
				pv = image[row, col, c]
				image[row, col, c] = 255 - pv

	# 输出的是一个呈现负片效果的图片
	cv.imshow("pixels_demo", image)


def create_image():
	"""创建新图象"""
	# 创建一张宽高都是400像素的3通道 8位图片
	img = np.zeros([400, 400, 3], np.uint8)
	# 修改通道值
	img[:, :, 0] = np.ones([400, 400]) * 255
	img[:, :, 2] = np.ones([400, 400]) * 255
	cv.imshow("new image", img)

	# 创建一个单通道的8位图片
	img = np.zeros([400, 400, 1], np.uint8)
	img = img * 127
	cv.imshow("new image", img)
	# cv.imwrite("127img.png", img)

	# numpy 数组维度的变换
	# 定义一个二维数组
	img = np.ones([3, 3], np.uint8)
	# 填充每个元素
	img.fill(1000.22)
	print(img)
	# 变换为一维数组
	img = img.reshape([1, 9])
	print(img)


# 读入图片文件
src = cv.imread('test.jpg')

# 获取cpu当前时钟总数
t1 = cv.getTickCount()
access_pixel(src)
t2 = cv.getTickCount()
# 计算处理像素花费的时间
# cv.getTickFrequency() 每秒的时钟总数
time = ((t2 - t1) / cv.getTickFrequency())
print("time: %s s" % time)
create_image()
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()