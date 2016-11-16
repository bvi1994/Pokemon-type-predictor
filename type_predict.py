# This program predicts the Pokemon type based on the base stats
# using decision trees from the sklearn library

from sklearn import tree
from sklearn import neural_network
from sklearn import naive_bayes
from sys import argv
import numpy as np
import csv
from random import randint
import warnings

def train_type_bayes(training_points):
    data_set = open('Pokemon.csv')
    pokemonFile = csv.reader(data_set)
    pokemonData = list(pokemonFile)
    length = len(pokemonData)

    X = []
    Y = []
#    Pokemon = []

    for _ in range(training_points):
        row = randint(1, length - 1)
        X.append(pokemonData[row][6:11])
        Y.append(pokemonData[row][2])
        X = [[int(x) for x in sublist] for sublist in X]
  
    data_set.close()
    clf = naive_bayes.GaussianNB()
    clf = clf.fit(X,Y)
#   prediction = clf.predict([[atk, defense, spec_atk, spec_def, speed]])

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # This is to get rid of the warnings the Ski-learn likes to print to. 
    return clf


def train_type_network(training_points):
    data_set = open('Pokemon.csv')
    pokemonFile = csv.reader(data_set)
    pokemonData = list(pokemonFile)
    length = len(pokemonData)

    X = []
    Y = []
#    Pokemon = []

    for _ in range(training_points):
        row = randint(1, length - 1)
        X.append(pokemonData[row][6:11])
        Y.append(pokemonData[row][2])
        X = [[int(x) for x in sublist] for sublist in X]
  
    data_set.close()
    clf = neural_network.MLPClassifier()
    clf = clf.fit(X,Y)
#   prediction = clf.predict([[atk, defense, spec_atk, spec_def, speed]])

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # This is to get rid of the warnings the Ski-learn likes to print to. 
    return clf

# script, atk, defense, spec_atk, spec_def, speed = argv
def train_type_trees(training_points):
    data_set = open('Pokemon.csv')
    pokemonFile = csv.reader(data_set)
    pokemonData = list(pokemonFile)
    length = len(pokemonData)

    X = []
    Y = []
#    Pokemon = []

    for _ in range(training_points):
        row = randint(1, length - 1)
        X.append(pokemonData[row][6:11])
        Y.append(pokemonData[row][2])
        X = [[int(x) for x in sublist] for sublist in X]
#        Y = Y.reshape(-1,1)
    #Pokemon.append(pokemonData[row][1])
    # We need to convert each element of the list of list of integers to actual integers
    # because the ints were originally str in .csv

# print(X)
# print(Y)
# print(Pokemon)    

    data_set.close()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X,Y)
#   prediction = clf.predict([[atk, defense, spec_atk, spec_def, speed]])

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # This is to get rid of the warnings the Ski-learn likes to print to. 
    return clf

#   print(prediction)

def predict_type(point, tree):
    prediction = tree.predict(point)
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    return prediction