import numpy as np
import cv2

c = cv2.VideoCapture(0)
while 1:
	ret, image = c.read()
	cv2.putText(image,'Handsome', (220, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (127, 127, 255), 2)
	cv2.imshow("Origin", image)
	key = cv2.waitKey(1)
	if key == 27:
		cv2.destroyAllWindows()
		break
# 等待用户操作
cv2.waitKey(0)
# 释放所有窗口
cv2.destroyAllWindows()