import cv2
import numpy as np 
from matplotlib import pyplot as plt 

title = "mul_4.jpg"
img = cv2.imread(title)


img = img.astype(int)
img = img * 5
#img = img.astype(np.uint8)

#cv2.imshow("salida",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite("out_mul"+title,img)
