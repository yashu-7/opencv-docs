import cv2
import numpy as np

def nothing(val):
    pass

def click(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(window,(int(x),int(y)),rd,(b,g,r),tck)
    elif event == cv2.EVENT_RBUTTONDOWN:
        window.fill(0)

cv2.namedWindow('window')
cv2.setMouseCallback('window',click)
window = np.zeros((480,640,3),dtype=np.uint8)
disp = window[0:50,590:640]

cv2.namedWindow('color')
cv2.resizeWindow('color',640,180)
cv2.createTrackbar('r','color',0,255,nothing)
cv2.createTrackbar('g','color',0,255,nothing)
cv2.createTrackbar('b','color',0,255,nothing)
cv2.createTrackbar('radius','color',1,50,nothing)
cv2.createTrackbar('thick','color',1,10,nothing)

run = True
while run:
    cv2.imshow('window',window)
    
    r = cv2.getTrackbarPos('r','color')
    g = cv2.getTrackbarPos('g','color')
    b = cv2.getTrackbarPos('b','color')
    rd = cv2.getTrackbarPos('radius','color')
    tck = cv2.getTrackbarPos('thick','color')

    disp[:] = [b,g,r]

    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        run = False

cv2.destroyAllWindows()