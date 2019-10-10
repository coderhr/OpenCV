import cv2

img = cv2.imread("lena.jpg")
px = img[100, 90]
print(px)
print(img.shape)
height, width, channels = img.shape
print(img.dtype)
print(type(img))
print(img.size)
face = img[100:200, 115:188]
cv2.namedWindow('hat', cv2.WINDOW_GUI_NORMAL )
'''cv2.imshow('face', face)
cv2.waitKey(0)

b, g, r = cv2.split(img)
print(b)
img = cv2.merge((b, g, r))

b = img[:, :, 0]
cv2.imshow("red", r)
cv2.waitKey(0)
cv2.imshow("green", g)
cv2.waitKey(0)
cv2.imshow("blue", b)
cv2.waitKey(0)'''

roi = img[25:120, 20:220, 2]
cv2.imshow("hat", roi)
cv2.waitKey(0)