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

img = cv2.imread("sub_1.jpg")
img2 = cv2.imread("sub_2.jpg")
row, col, channel = img.shape

img = img.astype(int)
img2 = img2.astype(int)

img = img/img2
aux = img.copy()
aux = aux*240
small = np.amin(img)
biggest= np.amax(img)

for i in range(row):
	for j in range(col):
		img[i,j] = (img[i,j]-small)*(255/(biggest-small)) + 0

img = img.astype(np.uint8)		
Th(img,row,col,170)
Th(aux,row,col,200)
cv2.imshow("ht_img",img)
cv2.imshow("ht_aux",aux)



#img = img * 5
#img = img.astype(np.uint8)

#cv2.imshow("salida",img) be carefull with imshow, 
# some times interprete tthe  date in order to show a more coherent output
#but it is different from the actuall imwrite method.
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("out_div.jpg",img)

fig = plt.figure(figsize=(10, 4))#may be size
ax1 = fig.add_subplot(1, 2, 1) #position
ax2 = fig.add_subplot(1, 2, 2) 

ax1.hist(img.ravel(),256,[0,256])
ax2.hist(aux.ravel(),256,[0,256])
plt.show()
