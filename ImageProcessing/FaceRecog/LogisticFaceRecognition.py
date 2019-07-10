import math
import numpy as np
import random
import os
import cv2

def crossValidation(dataset, k=5):
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / k)
    folds = []
    for i in range(k):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
    return folds

def predict(row,coef):
    x = coef[0]
    for i in range(len(row) - 1):
        x += coef[i+1] * row[i]
    return 1 / (1 + math.exp(-x))

def accuracy_score(pred,actual):
    count = 0
    for i in range(len(pred)):
        if actual[i] == pred[i]:
            count += 1
    return count / len(pred) * 100

def evaluateAlgorithm(dataset, epochs, alpha):
    scores = []
    folds = crossValidation(dataset)
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train, [])
        test = []
        for row in fold:
            rowcopy = list(row)
            rowcopy[-1] = None
            test.append(rowcopy)
        pred = logisticRegression(train, test, epochs, alpha)
        actual = [row[-1] for row in fold]
        score = accuracy_score(pred,actual)
        scores.append(score)
    return scores

def sgd(dataset,epochs,alpha):
    coef = [0] * len(dataset[0])
    for epoch in range(epochs):
        for row in dataset:
            pred = predict(row, coef)
            loss = pred - row[-1]
            coef[0] = coef[0] - alpha * loss
            for j in range(len(row) - 1):
                coef[j+1] = coef[j+1] - alpha * loss * row[j]
    return coef

def logisticRegression(train,test,epochs,alpha):
    coef = sgd(train,epochs,alpha)
    predictions = []
    for row in test:
        pred = predict(row,coef)
        predictions.append(round(pred))
    return predictions


current_dir = os.getcwd()
os.chdir(current_dir + '\\faces')
files = os.listdir()
faces = []
faceLength = [0]
users = {}

for i in range(len(files)):
    userName = files[i].split('.')[0]
    users[i] = userName

# print(users)

for file in files:
    face = np.load(file)
    face = face.reshape(face.shape[0], -1)
    faces.append(face)
    faceLength.append(len(face))

faces = np.vstack(faces)
faces = faces/255
labels = np.zeros((len(faces), 1))
partition = len(files)
# print(faceLength)
count = 0

slice_1 = 0
slice_2 = 0

for i in range(len(faceLength) - 1):
    slice_1 = faceLength[i]
    slice_2 = faceLength[i + 1]
    labels[slice_1:slice_2 + slice_1] = float(i)
# print(labels)

facesData = []
for i in range(len(faces)):
    facesData.append(np.append(faces[i], labels[i]))

facesData = np.asarray(facesData)

epochs = 5000
alpha = 0.01
acc_scores = evaluateAlgorithm(facesData,epochs, alpha)
print(acc_scores)

#avgScore = sum(acc_scores) / len(acc_scores)
#print(avgScore)
