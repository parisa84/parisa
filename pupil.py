import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib
#default : matplotlib.rcParams['figure.figsize'] = [6.0, 4.0]
matplotlib.rcParams['figure.figsize'] = [9.0, 6.0]


def equalize( img, a, b):
	gray = img.copy()
	gray = gray.astype(np.double) / np.max(gray)
	gray = 1-(1-gray)**a
	gray = (gray)**b
	gray = gray / np.max(gray)
	gray = gray * 255
	gray = gray.astype(np.uint8)
	#gray[gray > 256*2.0/3.0] = 255
	#gray = cv2.equalizeHist(gray)
	return gray


filename = "eye.jpg"

img = cv2.imread(filename)
gray = cv2.cvtColor( img, cv2.cv.CV_BGR2GRAY)

gray = equalize(gray, 30, 500)

circles = cv2.HoughCircles( gray, cv2.cv.CV_HOUGH_GRADIENT, 2.5, 100, minRadius=15, maxRadius=50)
print circles

if circles is not None:
	circles = np.round( circles[0,:]).astype("int")
	
	for (x,y,r) in circles:
		cv2.circle( img, (x,y), r, (0,0,255), 1)

while True:
	cv2.imshow('gray', gray)
	cv2.imshow('circles', img)
	if cv2.waitKey(1) == 27:
		break;

cv2.destroyAllWindows()