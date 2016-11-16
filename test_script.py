# This program runs type_predict.py as a test. Basically it gets training sets 
# which then the tree is built from type_predict.py and does a comparision
# to see if the predicted type is the same as the actual type. A plot of 
# number of training set vs correct prediction is then shown. 

import numpy as np
import matplotlib.pyplot as plt
import csv
import random
import type_predict as train

data_set = list(csv.reader(open('Pokemon.csv')))
correct_predict = 0
y = []
y1 = []
# error_predict = 0
# n = 10

for n in range(1,151):
    training_set = train.train_type(n) # Grab n data points for our training set
    for m in range(100):
        random_index = int(random.random() * 801)
        while random_index == 0:
            random_index = int(random.random() * 801)
        newType = data_set[random_index][2] # The actual Pokemon type
        newStats = data_set[random_index][6:11]
        newStats = [int(x) for x in newStats]
#        print(type(newStats))
        predicted_type = train.predict_type(newStats, training_set) # Predict the Pokemon type
        if predicted_type == newType:
            correct_predict += 1
#          print("Predicted type: ", predicted_type, "Actual type: ", newType)
#        else:
#            error_predict += 1
#    print("The number of correct out of 100 is ", correct_predict, "for ", n, " training data")
    y.append(correct_predict)
    if n % 5 == 0:
        y1.append(correct_predict)
    correct_predict = 0
#    error_predict = 0


x = np.arange(n)
x1 = np.arange(0, n, 5)

m, b = np.polyfit(x,y,1)
m1, b1 = np.polyfit(x1,y1,1)

plt.scatter(x, y)
plt.title('Number of Correct Prediction (out of 100) v. Number of Training Data')
plt.xlabel('Number of Training Data')
plt.ylabel('Number of correct predictions')
plt.plot(x, m*x+b, 'r-')
plt.legend(['y=%.2fx+%d' % (m, b)], loc='upper left')
# plt.plot(x1, m1*x1+b1, 'b-')
plt.show()

# print(m)
# print(m1)