import cv2
import numpy as np




lut = cv2.imread("colorStrips/256standard-strip.png")

im_gray = cv2.imread("1-256.png")
im_gray=np.uint8(im_gray)
dst = cv2.LUT(im_gray, lut)
cv2.imshow("colormap",dst)
cv2.imshow("normal",im_gray)
cv2.waitKey(0) 
cv2.destroyAllWindows() 