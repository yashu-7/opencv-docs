import cv2
import numpy as np

path = r'images\fields.jpeg'

img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray_img)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
img[dst>0.01*dst.max()]=[0,255,0]

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)