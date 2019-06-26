import numpy as np
import cv2

dataset = cv2.CascadeClassifier('data.xml')
capture = cv2.VideoCapture(0)

face_1 = np.load('faces/ravi.npy').reshape(50,50*50)
face_2 = np.load('faces/ravi.npy').reshape(50,50*50)

users = {0:"Ravi_1", 1:"Ravi_2"}

labels = np.zeros((100,1))
labels[50:,:] = 1.0

data = np.concatenate([face_1, face_2])
# print(data[:5].shape)

def distance(x2,x1):
    return np.sqrt(sum((x1 - x2) ** 2))

def knn(x,train,k=5):
    n = train.shape[0]
    d = []
    for i in range(n):
        d.append(distance(x,train[i]))
    d = np.asarray(d)
    indexes = np.argsort(d)
    sortedLabels = labels[indexes][:k]
    count = np.unique(sortedLabels, return_counts=True)
    return count[0][np.argmax(count[1])]

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray, 1.2)
        # print(faces)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (50,50))
            label = knn(face.flatten(), data)
            name = users[int(label)]
            cv2.putText(img, name, (x,y), font, 1, (255, 0, 0), 2)

        cv2.imshow('result',img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")

cv2.destroyAllWindows()
capture.release()