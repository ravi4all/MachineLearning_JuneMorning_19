import cv2

dataset = cv2.CascadeClassifier('data.xml')

capture = cv2.VideoCapture(0)
while True:
    ret,img = capture.read()
    if ret:
        faces = dataset.detectMultiScale(img, 1.2)
        # print(faces)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('result',img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")

cv2.destroyAllWindows()
capture.release()
