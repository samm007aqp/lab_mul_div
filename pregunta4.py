import cv2
import numpy as np 
from matplotlib import pyplot as plt 

def Th(img,row,col,x):
	for i in range(row):
		for j in range(col):
			val = img[i,j] 
			if val[0] > x:
				img[i,j] = 255
			else:
				img[i,j] = 0

img = cv2.imread("blending1.jpg")
img2 = cv2.imread("blend.jpg")
row, col, channel = img.shape
X = 0.3
img = img.astype(int)
img2 = img2.astype(int)

img = X*img + (1-X)*img2 

img = img.astype(np.uint8)		


cv2.imshow("salida",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("question4.jpg",img)

