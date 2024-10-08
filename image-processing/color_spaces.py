import cv2
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

print(len(flags))

def nothing(val):
    pass

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('color')

cv2.resizeWindow('color',640,230)
cv2.createTrackbar('hue_l','color',0,255,nothing)
cv2.createTrackbar('saturation_l','color',0,255,nothing)
cv2.createTrackbar('value_l','color',0,255,nothing)
cv2.createTrackbar('hue_u','color',0,255,nothing)
cv2.createTrackbar('saturation_u','color',0,255,nothing)
cv2.createTrackbar('value_u','color',0,255,nothing)

run = True
while run:
    ret,frame = cam.read()
    if not ret:
        run = False

    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    h_l = cv2.getTrackbarPos('hue_l','color')
    s_l = cv2.getTrackbarPos('saturation_l','color')
    v_l = cv2.getTrackbarPos('value_l','color')
    lower = np.array([h_l,s_l,v_l])
    
    h_u = cv2.getTrackbarPos('hue_u','color')
    s_u = cv2.getTrackbarPos('saturation_u','color')
    v_u = cv2.getTrackbarPos('value_u','color')
    upper = np.array([h_u,s_u,v_u])

    mask = cv2.inRange(frame,lower,upper)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('window',frame)
    cv2.imshow('window HSV',frame_hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        run = False

cv2.destroyAllWindows()
cam.release()