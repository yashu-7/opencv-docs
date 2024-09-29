import cv2
import numpy as np

def rclick(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(window,(int(x),int(y)),15,(0,255,0),2)
    elif event == cv2.EVENT_RBUTTONDOWN:
        window.fill(0)

cv2.namedWindow('window')
cv2.setMouseCallback('window',rclick)
window = np.zeros((480,640,3),dtype=np.uint8)

run = True
while run:

    cv2.imshow('window', window)

    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        run = False

cv2.destroyAllWindows()