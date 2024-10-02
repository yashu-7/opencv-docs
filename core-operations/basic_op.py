import cv2
import numpy as np
import matplotlib.pyplot as plt

window = np.zeros((480,640,3),dtype=np.uint8)

run = True
while run:
    cv2.imshow('window',window)

    pixel_val = window[0,0]
    # print(pixel_val)
    blue_pixel_val = window[0,0,0]
    # print(blue_pixel_val)

    b,g,r = cv2.split(window)

    # Converting to blue screen
    b = np.ones(b.shape,dtype=np.uint8)
    # print(b*255)
    b*=255

    # or
    b[:,:] = 255

    window1 = cv2.merge((b,g,r))


    # Region of intrest
    center_x,center_y = 320,240
    roi = window[310:330,230:250]
    print(roi.shape)

    window1[310:330,230:250] = roi
    window[0:20,0:20] = window1[0:20,0:20]
    cv2.imshow('window1', window1)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        run = False

cv2.destroyAllWindows()