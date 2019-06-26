import cv2
import numpy as np
import os

current_dir = os.getcwd()
facesPath = current_dir + '/faces'
# print(facesPath)
os.chdir(facesPath)
facesList = os.listdir()
# print(facesList)
facesArray = []
for i in range(len(facesList)):
    face = np.load(facesList[i])
    face = face.reshape(face.shape[0],-1)
    facesArray.append(face)

facesArray = np.asarray(facesArray)
facesArray = np.vstack(facesArray)

userName = {}
for i in range(len(facesList)):
    name = facesList[i].split(".")[0]
    userName[i] = name

labels = np.zeros((facesArray.shape[0], 1))
n = len(facesArray) // len(facesList)
for i in range(len(facesList)):
    labels[i*n:,:] = float(i)
# print(labels)

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
dataset = cv2.CascadeClassifier('../data.xml')
capture = cv2.VideoCapture(0)

while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        newFace = dataset.detectMultiScale(gray)
        # print(faces)
        for x, y, w, h in newFace:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (50,50))
            label = knn(face.flatten(), facesArray)
            name = userName[int(label)]
            cv2.putText(img, name, (x,y), font, 1, (255, 0, 0), 2)

        cv2.imshow('result',img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")

cv2.destroyAllWindows()
capture.release()
