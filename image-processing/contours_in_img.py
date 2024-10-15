import cv2
import numpy as np

img_path = r'images\forest.jpeg'

img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 15, 255, cv2.THRESH_BINARY_INV)

thresh = cv2.blur(thresh,(15,15))
thresh = cv2.GaussianBlur(thresh, (3,3), 2.5,2.5)

contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
print(len(cnt))

M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx,cy)

cv2.circle(img, (cx,cy), 15, (255,0,0), -1)

cv2.drawContours(img, contours, -1, (0,255,0), 1)

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),1)

cv2.imshow('img', img)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)