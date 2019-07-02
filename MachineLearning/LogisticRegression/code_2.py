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

def cross_validation():
    pass

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

def evaluateAlgorithm():
    pass

# stochastic gradient
def sgd():
    pass

def logisticRegression():
    pass

filename = 'data.csv'
dataset = load_Dataset(filename)
str_to_float(dataset)
minMaxValues = minMax(dataset)
normalization(minMaxValues)








