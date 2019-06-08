import cv2 as cv
import numpy as np

#摄像头操作
def video_demo():
	# 打开0号摄像头，捕捉该摄像头实时信息
	# 参数0代表摄像头的编号
	# 有多个摄像头的情况下，可用编号打开摄像头
	# 若是加载视频，则将参数改为视频路径，cv.VideoCapture加载视频是没有声音的，OpenCV只对视频的每一帧进行分析
	capture = cv.VideoCapture(0)
	if capture.isOpened() is False:  # 确认摄像头是否成功打开
		print('Error')
		exit(1)
	while (True):
		# 获取视频的返回值 ref 和视频中的每一帧 frame
		ref, frame = capture.read()

		# 加入该段代码将使拍出来的画面呈现镜像效果
		# 第二个参数为视频是否上下颠倒 0为上下颠倒 1为不进行上下颠倒
		frame = cv.flip(frame, 1)

		#给图像加文字
		# 参数1：图像,参数2：文字内容,参数3：坐标位置,参数4：字体,参数5：字号,参数6：颜色,参数7：字体粗细
		cv.putText(frame, 'Handsome', (220, 130), cv.FONT_HERSHEY_SIMPLEX, 2, (127, 127, 255), 2)

		# 将每一帧在窗口中显示出来
		cv.imshow("video", frame)

		# 设置视频刷新频率，单位为毫秒
		# 返回值为键盘按键的值
		c = cv.waitKey(50)

		# 27为 Esc 按键的返回值
		if c == 27:
			break


# 视频文件操作
def vidos_option(videoName):

	cap = cv.VideoCapture(videoName)  # 打开视频文件

	if cap.isOpened() is False:  # 确认视频是否成果打开
		print('Error')
		exit(1)

	frame_width = int(cap.get(3))  # 获取图片帧宽度
	frame_height = int(cap.get(4))  # 获取图像帧高度

	#  创建保存视频，指定保存视频名称，指定视频编码器，视频帧率，图像帧尺寸
	out = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))

	ret, frame = cap.read()  # 读取一帧图像，当视频帧读取完毕ret标识符为False
	while ret:
		cv.imshow('frame', frame)  # 显示图像帧
		cv.waitKey(20)  # 帧间隔为20ms
		frame = cv.flip(frame, 0)  # 对图像进行水平翻转
		out.write(frame)  # 将frame写入视频
		ret, frame = cap.read()  # 读取下一帧

	cap.release()
	out.release()


# 图片信息
def get_image_info(image):
	# 图像类别
	# 图像类别为numpy.dnarray,即n维数组
	print(type(image))

	# 获取图像通道数目
	# 返回值如：(900, 640, 3)
	# 这三个数字代表图片纵向像素、横向像素和通道数目
	print(image.shape)
	# 获取图像的高，宽以及深度。若图像是灰度或二值只返回高和宽
	im_height, im_width, im_dep = image.shape
	print('图片高为：%d,宽为：%d，深度为：%d' %(im_height,im_width,im_dep))
	# 图像总大小，计算公式为：长*宽*通道数目
	print('图像总大小:%d'%(image.size))

	# 每个像素点所占字节位数
	print('每个像素点所占字节位数:',image.dtype)

	# 提取ROI，10:100表示提取原图的第10行到第100行
	# 20:50表示提取原图的第20列到第50列
	# 第三个参数:表示提取所有通道，若只提取G通道则为1
	ROI = image[10:100, 20:50, :]
	# cv.imshow('New_ROI',ROI)






# 图像常用处理,不需要其中的内容时注释掉即可
def picOptions(image):
	# 获取图像的高，宽以及深度。若图像是灰度或二值只返回高和宽
	im_height, im_width, im_dep = image.shape

	# 1.转灰度图像
	# 常用的还有BGR转RGB（cv2.COLOR_BGR2RGB）等等
	# BGR转灰度图像，注意opencv读入的是BGR格式
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	cv.imshow('huidu',gray)

	# 2.图像二值化
	# cv2.shreshold函数第一个参数是输入图像，第二个参数是阈值，第三个参数是将超过阈值的像素值修改成设定值，
	# 第四个参数是具体实施方法，若改为cv2.THRESH_BINARY_INV就是将小于阈值的像素值修改成设定值，其他值为零，即反转
	threshold = 200
	ret,binary_image = cv.threshold(gray, threshold, 255, cv.THRESH_BINARY)  # 将灰度转为二值图像
	cv.imshow('2zhihua',binary_image)

	#3.图像的旋转
	M = cv.getRotationMatrix2D(( im_width/ 2, im_height/ 2), 90, 1)
	# M为旋转矩阵，第一个参数是设定旋转中心，第二个参数是旋转角度（单位是度，逆时针为正），第三个参数是缩放比例
	ratation = cv.warpAffine(image, M, (5000, 5000))
	cv.imshow('xuanzhuan',ratation)

	#4.图像的缩放
	# image为读入的图片， (width, height)为缩放后的尺寸， cv.INTER_NEAREST为采用最近邻插值
	# re_resize = cv.resize(image, (width, height), interpolation=cv.INTER_NEAREST)

	#5.图像轮廓操作
	# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 图像灰度化
	# ret, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)  # 图像二值化

	# 参数1：图像
	# 参数2：提取规则。cv.RETR_EXTERNAL：只找外轮廓，cv.RETR_TREE：内外轮廓都找。
	# 参数3：输出轮廓内容格式。cv.CHAIN_APPROX_SIMPLE：输出少量轮廓点。
	# cv.CHAIN_APPROX_NONE：输出大量轮廓点。；
	# 输出参数1：图像；输出参数2：轮廓列表；输出参数3：层级
	contours, hierarchy = cv.findContours(binary_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 获取轮廓

	# 若image是灰度或者二值图像将（255，0，0）改为任意灰度值，如200
	# 参数1：图像
	# 参数2：轮廓列表
	# 参数3：轮廓索引，如果负数则画出所有轮廓。
	# 参数4：轮廓颜色
	# 参数5：轮廓粗细
	cv.drawContours(image, contours, -1, (255, 0, 0), 3)  # 将所有轮廓全都绘制到image上，
	# cv.drawContours(image, [contours[2]], -1, (255, 0, 0), 3)  # 只绘制其中某一个轮廓
	cv.imshow('lunkuo', image)

	# 判断某一像素点是否在轮廓内
	# 参数1：某一轮廓列表
	# 参数2：像素点坐标
	# 参数3：如果为True则输出该像素点到轮廓最近距离。如果为False，则输出为正表示在轮廓内，0为轮廓上，负为轮廓外。
	# result = cv.pointPolygonTest(contours, (1000,1000), False)
	# print(result)




# 读入图片文件
src = cv.imread('test.jpg')
get_image_info(src)
# 将图片保存为 testSave.png
# cv.imwrite("testSave.png", src)
# 显示图片
cv.imshow('show',src)

# 调用图片常用处理操作函数
picOptions(src)

#摄像头屏幕显示
# video_demo()
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()