from skimage.filters import threshold_local
import numpy as np
import cv2
import imutils

def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")

	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	# return the ordered coordinates
	return rect

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	# return the warped image
	return warped

def magic_clean(img):
	image = cv2.imread(img)
	print(image.shape)
	#orig_im = image.copy()
	#gray_im = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#gray_im = cv2.GaussianBlur(gray_im,(5,5),0)
	#edge_im = cv2.Canny(gray_im,75,100)
	# contours_im = cv2.findContours(edge_im.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	# contours_im = imutils.grab_contours(contours_im)
	# contours_im = sorted(contours_im, key = cv2.contourArea, reverse = True)[:5]
	# for c in contours_im:
	# 	# approximate the contour
	# 	peri = cv2.arcLength(c, True)
	# 	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# 	print(len(approx))
	# 	# if our approximated contour has four points, then we
	# 	# can assume that we have found our screen
	# 	if len(approx) == 4:
	# 		screenCnt = approx
	# 		break
	# cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
	# warped = four_point_transform(orig_im, screenCnt)
	# warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
	# T = threshold_local(warped, 11, offset = 10, method = "gaussian")
	# final_im = (warped > T).astype("uint8") * 255
	# return final_im
	edge_im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	T = threshold_local(edge_im, 11, offset = 10, method = "gaussian")
	final_im = (edge_im > T).astype("uint8") * 255
	return final_im
