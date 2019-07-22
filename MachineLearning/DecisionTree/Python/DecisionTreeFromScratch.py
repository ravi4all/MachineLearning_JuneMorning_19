#Evaluate Algo
#Cross Validation
#Accuracy Metric
#Random Forest
#bagging_predict
#Subsample
#BuildTree
#Get Split
#Split
#to_terminal
#gini index
#predict


#seeding the generated number makes our results reproducible (good for debugging)
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
 
# Convert string column to float
def str_column_to_float(dataset, column):
    #iterate throw all the rows in our data matrix
	for row in dataset:
        #for the given column index, convert all values in that column to floats
		row[column] = float(row[column].strip())
 
# Convert string column to integer
def str_column_to_int(dataset, column):
    #store a given column 
    class_values = [row[column] for row in dataset]
    #create an unordered collection with no duplicates, only unique valeus
    unique = set(class_values)
    #init a lookup table
    lookup = dict()
    #for each element in the column
    for i, value in enumerate(unique):
        #add it to our lookup table
        lookup[value] = i
    #the lookup table stores pointers to the strings
    for row in dataset:
        row[column] = lookup[row[column]]
    #return the lookup table
    return lookup

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

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    #init 2 empty lists for storing split dataubsets
	left, right = list(), list()
    #for every row
	for row in dataset:
        #if the value at that row is less than the given value
		if row[index] < value:
            #add it to list 1
			left.append(row)
		else:
            #else add it list 2 
			right.append(row)
    #return both lists
	return left, right
 
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
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores
 
 
# Calculate the Gini index for a split dataset
## this is the name of the cost function used to evaluate splits in the dataset.
# this is a measure of how often a randomly chosen element from the set 
#would be incorrectly labeled if it was randomly labeled according to the distribution
#of labels in the subset. Can be computed by summing the probability
#of an item with label i being chosen times the probability 
#of a mistake in categorizing that item. 
#It reaches its minimum (zero) when all cases in the node 
#fall into a single target category.
#A split in the dataset involves one input attribute and one value for that attribute. 
#It can be used to divide training patterns into two groups of rows.
#A Gini score gives an idea of how good a split is by how mixed the classes 
#are in the two groups created by the split. A perfect separation results in 
#a Gini score of 0, whereas the worst case split that results in 50/50 classes 
#in each group results in a Gini score of 1.0 (for a 2 class problem).
#We first need to calculate the proportion of classes in each group.
def gini_index(groups, class_values):
	gini = 0.0
    #for each class
	for class_value in class_values:
        #a random subset of that class
		for group in groups:
			size = len(group)
			if size == 0:
				continue
            #average of all class values
			proportion = [row[-1] for row in group].count(class_value) / float(size)
            #  sum all (p * 1-p) values, this is gini index
			gini += (proportion * (1.0 - proportion))
	return gini
 
# Select the best split point for a dataset
#This is an exhaustive and greedy algorithm
def get_split(dataset, n_features):
    ##Given a dataset, we must check every value on each attribute as a candidate split, 
    #evaluate the cost of the split and find the best possible split we could make.
	class_values = list(set(row[-1] for row in dataset))
	b_index, b_value, b_score, b_groups = 999, 999, 999, None
	features = list()
	while len(features) < n_features:
		index = randrange(len(dataset[0])-1)
		if index not in features:
			features.append(index)
	for index in features:
		for row in dataset:
            ##When selecting the best split and using it as a new node for the tree 
            #we will store the index of the chosen attribute, the value of that attribute 
            #by which to split and the two groups of data split by the chosen split point.
            ##Each group of data is its own small dataset of just those rows assigned to the 
            #left or right group by the splitting process. You can imagine how we might split 
            #each group again, recursively as we build out our decision tree.
			groups = test_split(index, row[index], dataset)
			gini = gini_index(groups, class_values)
			if gini < b_score:
				b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    ##Once the best split is found, we can use it as a node in our decision tree.
    ##We will use a dictionary to represent a node in the decision tree as 
    #we can store data by name. 
	return {'index':b_index, 'value':b_value, 'groups':b_groups}
 
# Create a terminal node value

def to_terminal(group):
    #select a class value for a group of rows. 
	outcomes = [row[-1] for row in group]
    #returns the most common output value in a list of rows.
	return max(set(outcomes), key=outcomes.count)
 
#Create child splits for a node or make terminal
#Building a decision tree involves calling the above developed get_split() function over 
#and over again on the groups created for each node.
#New nodes added to an existing node are called child nodes. 
#A node may have zero children (a terminal node), one child (one side makes a prediction directly) 
#or two child nodes. We will refer to the child nodes as left and right in the dictionary representation 
#of a given node.
#Once a node is created, we can create child nodes recursively on each group of data from 
#the split by calling the same function again.
def split(node, max_depth, min_size, n_features, depth):
    #Firstly, the two groups of data split by the node are extracted for use and 
    #deleted from the node. As we work on these groups the node no longer requires access to these data.
	left, right = node['groups']
	del(node['groups'])
    
    #Next, we check if either left or right group of rows is empty and if so we create 
    #a terminal node using what records we do have.
	# check for a no split
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right)
		return
    #We then check if we have reached our maximum depth and if so we create a terminal node.
	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
    #We then process the left child, creating a terminal node if the group of rows is too small, 
    #otherwise creating and adding the left node in a depth first fashion until the bottom of 
    #the tree is reached on this branch.
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
	else:
		node['left'] = get_split(left, n_features)
		split(node['left'], max_depth, min_size, n_features, depth+1)
	# process right child
    #The right side is then processed in the same manner, 
    #as we rise back up the constructed tree to the root.
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
	else:
		node['right'] = get_split(right, n_features)
		split(node['right'], max_depth, min_size, n_features, depth+1)
 
#Build a decision tree
def build_tree(train, max_depth, min_size, n_features):
    #Building the tree involves creating the root node and 
	root = get_split(train, n_features)
    #calling the split() function that then calls itself recursively to build out the whole tree.
	split(root, max_depth, min_size, n_features, 1)
	return root
 
# Make a prediction with a decision tree
def predict(node, row):
    #Making predictions with a decision tree involves navigating the 
    #tree with the specifically provided row of data.
    #Again, we can implement this using a recursive function, where the same prediction routine is 
    #called again with the left or the right child nodes, depending on how the split affects the provided data.
    #We must check if a child node is either a terminal value to be returned as the prediction
    #, or if it is a dictionary node containing another level of the tree to be considered.
	if row[node['index']] < node['value']:
		if isinstance(node['left'], dict):
			return predict(node['left'], row)
		else:
			return node['left']
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']
 
# Create a random subsample from the dataset with replacement
def subsample(dataset, ratio):
	sample = list()
	n_sample = round(len(dataset) * ratio)
	while len(sample) < n_sample:
		index = randrange(len(dataset))
		sample.append(dataset[index])
	return sample


# Make a prediction with a list of bagged trees
#responsible for making a prediction with each decision tree and 
#combining the predictions into a single return value. 
#This is achieved by selecting the most common prediction 
#from the list of predictions made by the bagged trees.
def bagging_predict(trees, row):
	predictions = [predict(tree, row) for tree in trees]
	return max(set(predictions), key=predictions.count)
 
# Random Forest Algorithm
#esponsible for creating the samples of the training dataset, training a decision tree on each,
#then making predictions on the test dataset using the list of bagged trees.
def random_forest(train, test, max_depth, min_size, sample_size, n_trees, n_features):
	trees = list()
	for i in range(n_trees):
		sample = subsample(train, sample_size)
		tree = build_tree(sample, max_depth, min_size, n_features)
		trees.append(tree)
	predictions = [bagging_predict(trees, row) for row in test]
	return(predictions)
 
# Test the random forest algorithm
seed(1)
# load and prepare data
filename = 'german_credit.csv'
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(0, len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# evaluate algorithm
n_folds = 5
max_depth = 10
min_size = 1
sample_size = 1.0
n_features = int(sqrt(len(dataset[0])-1))
for n_trees in [1, 5, 10]:
	scores = evaluate_algorithm(dataset, random_forest, n_folds, max_depth, min_size, sample_size, n_trees, n_features)
	print('Trees: %d' % n_trees)
	print('Scores: %s' % scores)
	print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))