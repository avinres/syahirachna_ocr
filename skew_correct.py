import numpy as np
import cv2

def deskew(img):
	#gray = img
	image = img
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	img = cv2.bitwise_not(gray)
	thresh = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	coords = np.column_stack(np.where(thresh>0))
	angle = cv2.minAreaRect(coords)[-1]
	if angle < -45:
		angle = -(90 + angle)
	else :
		angle = -angle
	
	(h,w,_) = image.shape
	#(h,w) = image.shape[:2]
	center = (w//2,h//2)
	M = cv2.getRotationMatrix2D(center, angle, 1.0)
	rotated = cv2.warpAffine(image, M, (w, h),
		flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

	return rotated