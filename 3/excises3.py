import cv2

capture = cv2.VideoCapture('cut.mp4')

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
outfile = cv2.VideoWriter('output.avi', fourcc, 25, (1920, 1080))

while(capture.isOpened()):
    status, frame = capture.read()
    if status:
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        print(frame.shape)
        cv2.imshow('frame', frame)
        outfile.write(frame)
        if cv2.waitKey(20) == ord('q'):
            break
