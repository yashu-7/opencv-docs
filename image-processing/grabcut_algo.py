import cv2
import numpy as np


x1, y1, x2, y2 = -1, -1, -1, -1
drawing = False  
rectangle_complete = False 
rect = None


def lclick(event, x, y, flags, params):
    global x1, y1, x2, y2, drawing, rectangle_complete, img_copy, rect

    if event == cv2.EVENT_LBUTTONDOWN:
        if not drawing and not rectangle_complete:
            x1, y1 = x, y
            drawing = True
        elif rectangle_complete:
            rectangle_complete = False
            img_copy = img.copy()

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            x2, y2 = x, y
            cv2.rectangle(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            x2, y2 = x, y
            drawing = False
            rectangle_complete = True

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            img_copy = img.copy()  
            rect = (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))  

img_path = r'images\lake.jpeg'
img = cv2.imread(img_path)
img_copy = img.copy()

mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

cv2.namedWindow('lake')
cv2.setMouseCallback('lake', lclick)

run = True
while run:
    if rectangle_complete and rect is not None:
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 25, cv2.GC_INIT_WITH_RECT)
        
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        output = img * mask2[:, :, np.newaxis]

        cv2.imshow('the cut image', output)
    
    cv2.imshow('lake', img_copy)
    
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        run = False

cv2.destroyAllWindows()