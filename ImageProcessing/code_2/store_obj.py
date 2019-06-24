import cv2
import numpy as np

cap = cv2.VideoCapture(0)

data = []
while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        roi = frame[100:300, 100:300]
        cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
        obj = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        fc = cv2.resize(obj, (50,50))

        #print(obj)
        if len(data) < 200:
            data.append(fc)
            # print(len(data))

        cv2.imshow('frame',frame)
        cv2.imshow('gray',obj)
        k = cv2.waitKey(30) & 0xFF
        if k == 27 or len(data) >= 200:
            break
    else:
        print("Camera not working")

data = np.asarray(data)
np.save('bottle.npy',data)
cap.release()
cv2.destroyAllWindows()
