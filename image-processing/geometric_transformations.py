import cv2
import numpy as np

img_path = r'images/sea.jpeg'

img = cv2.imread(img_path)

print(img.shape)

res = cv2.resize(img, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_CUBIC)

cv2.imshow('image', img)
cv2.imshow('res', res)
cv2.waitKey(0)

# Translation

new_x = 50
new_y = 50

array = np.array([[1,0,new_x],[0,1,new_y]],dtype=np.float32)
dst = cv2.warpAffine(img,array,(img.shape[1],img.shape[0]))

cv2.imshow('Translation image',dst)
cv2.waitKey(0)

# Rotation

M = cv2.getRotationMatrix2D(((img.shape[1]-1)/2.0,(img.shape[0]-1)/2.0),15,1)
# M = cv2.getRotationMatrix2D((0,0),-45,1)
dst = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

cv2.imshow('rotated image', dst)
cv2.waitKey(0)

# Affine transformation

pnts1 = np.float32([[50,0],[50,50],[10,0]])
pnts2 = np.float32([[100,50],[80,80],[100,90]])

M = cv2.getAffineTransform(pnts1,pnts2)
dst = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

cv2.imshow("Affine image",dst)
cv2.waitKey(0)

# Perspective transform

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
 
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))

cv2.imshow("Perspective image",dst)
cv2.waitKey(0)


cv2.destroyAllWindows()