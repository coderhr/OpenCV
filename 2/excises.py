import cv2
img = cv2.imread('lena.jpg', 1)
cv2.namedWindow('lena2', cv2.WINDOW_NORMAL)
cv2.imshow('lena2', img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('huang.png', img)
