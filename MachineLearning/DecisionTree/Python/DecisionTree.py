from random import seed
from random import randrange
from csv import reader
from math import sqrt

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
def str_to_float(dataset):
    for row in dataset:
        for col in range(len(row)):
            row[col] = float(row[col])
 

def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

 
# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0
 
# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
        #add each row in a given subsample to the test set
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
#        print(predicted)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores


def gini_index(class_values, groups):
    gini = 0.0
    
    # for each class
    for class_value in class_values:
        # a random subset of that class
        for group in groups:
            size = len(group)
            # to avoid divide by zero
            if size == 0:
                continue
            
            # average of all class values
            proportion = [row[-1] for row in group].count(class_value) / float(size)
            gini += (proportion * (1.0 - proportion))
            
    return gini

def test_split(value,index, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
            

def get_split(dataset, n_features):
    
    class_values = list(set([row[-1] for row in dataset]))
    b_index, b_value, b_score, b_groups = 999,999,999,None
    features = list()
    
    while len(features) < n_features:
        index = randrange(len(dataset[0] - 1))
        if index not in features:
            features.append(index)
    
    for index in features:
        for row in dataset:
            groups = test_split(row[index], index, dataset)
            gini = gini_index(class_values, groups)
            
            if gini < b_score:
#                print(gini)
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
                
                
    return {'index':b_index,'value':b_value, 'groups':b_groups}

def to_terminal():
    pass

def split():
    pass

def build_tree():
    pass

def predict():
    pass

def bagged_predict():
    pass

def random_forest():
    pass


dataset = [
         [2.7810836,2.550537003,0],
     	[1.465489372,2.362125076,0],
     	[3.396561688,4.400293529,0],
     	[1.38807019,1.850220317,0],
     	[3.06407232,3.005305973,0],
     	[7.627531214,2.759262235,1],
     	[5.332441248,2.088626775,1],
     	[6.922596716,1.77106367,1],
     	[8.675418651,-0.242068655,1],
     	[7.673756466,3.508563011,1]
     ]
# str_to_float(dataset)

n_folds = 5
max_depth = 10
min_size = 1
sample_size = 1.0
n_features = int(sqrt(len(dataset[0])-1))
print("Number of features",n_features)

for n_trees in [1, 5, 10]:
	scores = evaluate_algorithm(dataset, random_forest, n_folds, max_depth, min_size, sample_size, n_trees, n_features)
	print('Trees: %d' % n_trees)
	print('Scores: %s' % scores)
	print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))