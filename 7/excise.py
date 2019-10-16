import cv2
import matplotlib.pyplot as plt
import numpy as np

'''img = cv2.imread('huang.png')

res = cv2.resize(img, (132, 150))

res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imshow('shrink', res)
cv2.waitKey(0)
cv2.imshow('zoom', res2)
cv2.waitKey(0)
img = img[:,:,[2,1,0]]
dst = cv2.flip(img, 1)
dst1 = cv2.flip(img, -1)
dst2 = cv2.flip(img, 0)
titles = ['Original', "horizontal", 'vertical', 'horizontalAndVertical']
images = [img, dst, dst1, dst2]
#cv2.imshow("shuipin", dst)
#cv2.waitKey(0)
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i], fontsize = 8)
    plt.xticks([]), plt.yticks([])

plt.show()'''

img = cv2.imread('huang.png')
rows, cols = img.shape[:2]
'''M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('shift', dst)
cv2.waitKey(0)'''

M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('rotation', dst)
cv2.waitKey(0)