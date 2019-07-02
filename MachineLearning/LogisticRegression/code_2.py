import math
import random
import csv

def load_Dataset(path):
    dataset = []
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row)
    return dataset

def str_to_float(dataset):
    for row in range(len(dataset)):
        for col in range(len(dataset[row])):
            dataset[row][col] = float(dataset[row][col])

def minMax(dataset):
    minMaxValues = []
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        minValue = min(col_values)
        maxValue = max(col_values)
        minMaxValues.append([minValue, maxValue])
    return minMaxValues

def normalization(minMaxData):
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            numer = dataset[i][j] - minMaxData[j][0]
            denom = minMaxData[j][1] - minMaxData[j][0]
            dataset[i][j] = numer/denom

def cross_validation(dataset,k=5):
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
    
def prediction(row,coef):
    x = coef[0]
    for i in range(len(row) - 1):
        x += coef[i+1] * row[i]
    return 1 / (1 + math.exp(-x))

def accuracy_score(pred,actual):
    count = 0
    for i in range(len(pred)):
        if pred[i] == actual[i]:
            count += 1
    return count / len(pred) * 100

def evaluateAlgorithm(epochs,learning_rate,dataset):
    folds = cross_validation(dataset)
    scores = []
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train,[])
        test = []
        for row in fold:
            rowcopy = list(row)
            rowcopy[-1] = None
            test.append(rowcopy)
        predictions = logisticRegression(train,test,epochs,learning_rate)
        actual = [row[-1] for row in fold]
        score = accuracy_score(predictions, actual)
        scores.append(score)
    return scores

# stochastic gradient
def sgd(dataset,epochs,learning_rate):
    b = [0] * len(dataset[0])
    for i in range(epochs):
        for row in dataset:
            y_pred = prediction(row,b)
            loss = y_pred - row[-1]
            b[0] = b[0] - learning_rate * loss
            for j in range(len(row) - 1):
                b[j+1] = b[j+1] - learning_rate * loss * row[j]
    return b
    

def logisticRegression(train,test,epochs,learning_rate):
    coef = sgd(train,epochs,learning_rate)
    predictions = []
    for row in test:
        pred = prediction(row,coef)
        predictions.append(round(pred))
    return predictions

filename = 'data.csv'
dataset = load_Dataset(filename)
str_to_float(dataset)
minMaxValues = minMax(dataset)
normalization(minMaxValues)

epochs = 10000
learning_rate = 0.01
scores = evaluateAlgorithm(epochs,learning_rate,dataset)
print(scores)






