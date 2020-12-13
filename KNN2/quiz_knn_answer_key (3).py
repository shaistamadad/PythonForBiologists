
# This implements a simple version of a k-nearest neighbour model for k=1
# iris_train.tsv is a tab-separated file with training data to predict a species of iris. 
# The first column is petal length in mm; the second column is petal width in mm; the third column is the species.
# Each row is data from a separate flower.
# iris_test.tsv is an independent test set.

import sys
import numpy as np
import pdb # need to import the built-in python debugger 
# (1) a function distance_euc(v1, v2) which computes the (squared) Euclidean distance between two sequences (Euclidean distance is the sum of the squared element-wise differences).
def distance_euc(v1, v2):
    assert len(v1) == len(v2),  "vectors wrong length"
    d = 0.0
    for i in range(len(v1)):
        d = d + (v1[i]-v2[i])**2
    return d


# (2) A function knn_train(m, x_train, y_train) where m is a list data structure for the knn model, and where x is the training data explanatory variables and y is the training data labels. m is passed by reference and is modified to store x_train and y_train.
def knn_train(m, x_train, y_train):
    m.append(x_train)
    m.append(y_train)

# (3) A function knn_predict(m, x_test) where x_test is a sequence of explanatory variables, which returns a sequence of predictions, one for each row of data.
def knn_predict(m, x_test):
    breakpoint # placed a debugger at the start of my function
    """This function takes in two files m and x-test. m is a list of two lists. The first list in m  is a list of 16 2-length vectors in an array, representing 
    the petal length and petal width. The second list in m is a list of 16 labels for each of the 2-length vectors in list 1 of m. k_test is a list of 
    6 two-length vectors, whose labels we will need to predict. This function implements the 3-nearest neighbour model. It will take the three 
    nearest data points  from the training data( distance between a test data point and the training data points is measured using the euclidean distance 
    function above) , and look at the labels (setosa or versicolor) of the three nearest points to decide the label for the test set """ 
    predictions = []  # an empty list. This will be filled with 6 predictions for each of the data point of test_data. Function will return this list 
    Top3= list()  # I have created a list of empty lists. After the for loop, Top3 will be filled with 96 euclidean distances, 16 each for 6 of the test_data points 
    for i in range(len(x_test)): # which is 6 
        import sys
        best_match = sys.float_info.max  # sys.float_info.max is the biggest possible number. As you run the for loop, each euclidean distance is compared with d, and if d is bigger than that number, d is replaced with the smaller number. so d starts out as the highest possible number, and it then becomes the lowest possible number by the time the for loop ends. This is used here to compared d with the euclidean distance between each test point the the 16 data points. For each point ,if the distance is smaller than sys_float.info.max, the number will replace it and the number itself will be repalced if the next euclidean distance is smaller  
        best_match_index = list() # create an empty list. This will be filled with 18 index numbers in total, three for each of the 6 x_test vectors. 
        for j in range(len(m[0])): # which is 16 
            d = distance_euc(m[0][j], x_test[i])
            Top3.append(d)    
    Top31=np.array(Top3)  # an array containing all the 16 distances for each of the 6 points 
    TopThreeDistances1=np.array_split(Top31, len(x_test))  # create a list of 6 arrays: each array contains 16 vector points for each of the 6 x_test vectors            
    TopThreeDistances2 = list()  # create an empty list  
    TopThreeDistances2= TopThreeDistances1.copy()  # here I have created a copy of my list of arrays. I will sort this copy of my list of arrays as I need the original unsorted copy for later. 
    for i in range(len(TopThreeDistances1)): #which is 6 
        TopThreeDistances2[i] = np.sort(TopThreeDistances2[i])  # so TopThreeDistances2 is now a list of arrays. In each array, the 16 euclidean distances are now arranged from smallest to the biggest. 
    #print(len(TopThreeDistances2))
    #print(type(TopThreeDistances1[1][0]))
    #print(type(TopThreeDistances2[1][0]))
    #print(TopThreeDistances2[0])
    #print(TopThreeDistances2[1])
    #print(TopThreeDistances[2])
    #print(TopThreeDistances[3])
    for i in range(len(TopThreeDistances2)):  # This for loop will get a list of indexes for each of my test points. The indexes represent the position of those  vectors in the first list of the m file which give three smallest euclidean  distances  for  each of the 6 test points. 
        for j in range(len(m[0])): #which is 16 
            if TopThreeDistances2[i][0]==TopThreeDistances1[i][j]:    # for the first distance in each sorted array of TopThreeDistances2, find the distance in the corresponding unsorted array in TopThreeDistances1
                #print(TopThreeDistances1[i][0])
                #print(TopThreeDistances2[i][j])
                best_match_index.append(j)  # once I find the corresponding distance in the unsorted array of TopThreeDistances1, append the index of the vector for that distance in the original m file to the best_match_index list 
                #print(j)
                break     # the break is important in order to choose only the first instance of a match with the smallest distance, so that the for loop terminates at the first instance of the condition being met, otherwise we might get more than one index for each smallest distance in the sorted arrays of TopThreeDistances2 
        for j in range(len(m[0])):   # do the same procedure as above, but this time to find the index of the second smallest number for each of  array in the sorted array  (TopThreeDistances2)
            if TopThreeDistances2[i][1]==TopThreeDistances1[i][j]:
                best_match_index.append(j)
                #print(j)
                break 
        for j in range(len(m[0])):
            if TopThreeDistances2[i][2]==TopThreeDistances1[i][j]:  # do the same same procedure as above, but this time to find the index, in the first list of the m file, of the  vector which gives the third smallest euclidean distance with a given data x_test data point 
                best_match_index.append(j)
                #print(j)
                break
    #print(best_match_index)
    index_array= np.array(best_match_index) #convert data type of best_match_index from list to an array. This array with 18 index numbers will be further split into 6 groups using the convenient array split function  
    index_array1= np.array_split(best_match_index, len(x_test))  # now I need to divide my array into a list of 6 arrays, each array contains 3 indexes for each of the 6 x_test data points 
    #print(index_array1)
    #print(index_array1[0][0])
    for i in range(len(x_test)):   # now that I have the 3 indexes corresponding to the vector positions, in the  first list of m file, which give  the three smallest euclidean distances for each vector of test data, I need to find the corresponding label for the vectors from the second list in m file. 
        for j in range(3):    # since three index numbers in each array of index_array1
            number1=0
            number2=0
            if m[1][index_array1[i][j]]== 'setosa':   #index_array1[i][j] represents the index number in the m list for the three vectors which give the three smallest euclidean distances 
                number1= number1+1    # so if, at the given index for the m[1] which represent the labels in the seconf list of training m file, the label is setosa, number1 should increase by 1 
            if m[1][index_array1[i][j]]== 'versicolor':   # if, at the given index, the corresponding m[1] label is versicolor, number2 should increase by 1 
                number2= number2+1 
        if number1>number2:    # here I am employing a voting mechanism. If out of the three cases, if two or more are setosa, number1 will be 2 (or 3), number2 will be 1(or 0), so number1>number2, hence I add "setosa" to the empty list: predictions 
            predictions.append("setosa")
        elif number2>number1:  # if out of the three cases, atleast two are versicolor, number2>number1, hence 'versicolor' will be added as a prediction to the list predictions 
            predictions.append("versicolor")

         # in the end, we get a list called predictions, which will contain a label for each of the six vectors of the x_test dataset 
    
    
    return predictions

# (4) Define the data structure for the model and use these functions to train the model on the data in "iris_train.tsv", then predict the labels for the test data in "iris_test.tsv" and print them.

m = []  # for our model we will use a two-element list

# train model with training data, then predict labels of independent test set, and print predictions
with open("iris_train.tsv", "r") as f:
    x_train = [];
    y_train = [];
    data = f.readlines()
    for i in range(len(data)):
        s = data[i].strip().split('\t')
        y_train.append(s[-1])
        x_train.append(s[:-1])
        x_train[i] = [float(i) for i in x_train[i] ]

with open("iris_test.tsv", "r") as f:
    x_test = [];
    data = f.readlines()
    for i in range(len(data)):
        x_test.append(data[i].strip().split('\t'))
        x_test[i] = [float(i) for i in x_test[i] ]

knn_train(m, x_train, y_train)
p = knn_predict(m, x_test)
print(p)
print("\n")

# (5) A custom class called "knn_class" which can be used in the following way:
# a = knn_class(x_train, y_train)
# pred = a.predict(x_test)

class knn_class:
    def __init__(self, x_train, y_train):
        self.m = []
        self.m.append(x_train)
        self.m.append(y_train)

    def predict(self, x_test):
        return knn_predict(self.m, x_test)

a = knn_class(x_train, y_train)
pred = a.predict(x_test)
print("class-based:")
print(pred)


