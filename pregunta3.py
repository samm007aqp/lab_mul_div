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

img = cv2.imread("sub_10.jpg")
img2 = cv2.imread("sub_11.jpg")
row, col, channel = img.shape

img = img.astype(int)
img2 = img2.astype(int)


img = img/img2 
aux = np.amax(img)
aux = int(255/aux)
img = img * aux
img = img.astype(np.uint8)		


cv2.imshow("salida",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("question3.jpg",img)

