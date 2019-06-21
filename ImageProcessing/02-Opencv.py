import cv2

capture = cv2.VideoCapture(0)
i = 0
while True:
    ret,img = capture.read()
    if ret:
        cv2.imshow('result',img)
        print(img)
        i += 1
        cv2.imwrite('img_{}.png'.format(i), img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")

cv2.destroyAllWindows()
capture.release()
