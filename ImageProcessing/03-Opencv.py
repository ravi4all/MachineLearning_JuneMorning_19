import cv2
cap = cv2.VideoCapture('video_1.mp4')
while True:
    ret, img = cap.read()
    img = cv2.resize(img, None, fx=0.5, fy=0.5)
    if ret:
        if cv2.waitKey(2) == 27:
            break
        cv2.imshow('result',img)
    else:
        print("Some error")

cv2.destroyAllWindows()
cap.release()
