import cv2

img = cv2.imread('lena.jpg')

#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flags)

capture = cv2.VideoCapture("cut.mp4")

lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

while(True):
    ret, frame = capture.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.cvtColor(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q'):
        break