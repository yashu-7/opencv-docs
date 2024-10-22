import cv2
import matplotlib.pyplot as plt

img_path = r'images\forest.jpeg'
template_path = r'images\template.jpg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
temp = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

w,h = temp.shape[::-1]

img2 = img.copy()

methods = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR',
 'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = getattr(cv2, meth)

res = cv2.matchTemplate(img, temp, method)
print(res)

xmin_val, xmax_val, min_loc, max_loc = cv2.minMaxLoc(res)

print(xmin_val,xmax_val,min_loc,max_loc)
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right,(255,255,255),2)


plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(meth)

plt.show()