import cv2
import numpy as np

drawing = False
x1, y1 = -1, -1

def draw_rect(event, x, y, flags, params):
    global x1, y1, drawing, img, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y  

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img = img_copy.copy()  
            cv2.rectangle(img, (x1, y1), (x, y), (0, 255, 0), 2)  
            cv2.imshow('forest', img)  

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img_copy, (x1, y1), (x, y), (0, 255, 0), 2)

        x_start, x_end = min(x1, x), max(x1, x)
        y_start, y_end = min(y1, y), max(y1, y)

        padding = 2
        x_start, x_end = max(0, x_start + padding), min(img.shape[1], x_end - padding)
        y_start, y_end = max(0, y_start + padding), min(img.shape[0], y_end - padding)

        roi = img_copy[y_start:y_end, x_start:x_end]

        if roi.size > 0:  
            cv2.imshow('roi', roi)
            cv2.imwrite(r'images/template.jpg',roi)  
        cv2.imshow('forest', img_copy)  

img_path = r'images/forest.jpeg'
img = cv2.imread(img_path)
img_copy = img.copy()  

cv2.namedWindow('forest')
cv2.setMouseCallback('forest', draw_rect)

run = True
while run:
    cv2.imshow('forest', img)  

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):  
        run = False

cv2.destroyAllWindows()