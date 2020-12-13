#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd Downloads


# In[419]:


def distance_euc(v1,v2):
    """This function takes as an inputs 2 two-dimension vector: and x and y points of co-ordinates 
    of the graph. This function then calculates the euclidean distance between the two points"""
    
    assert len(v1)==len(v2), "length of the two vectors should be equal: 2"

    distances=[]  # start with an empty list 
    x1=v1[0]  # the x co-ordinate of a given row of test data
    x2=v2[0] #the x coordinate of a given row of training data  
    y1= v1[1]  # y co-ordinate of a given row of test data
    y2= v2[1]  #y coordinate of a given row of training data 
    distances.append(((x1-x2)**2) + ((y2-y1)**2))  # formula to calculate the Euclidean distance 
    return distances


# In[420]:


import pandas as pd
import numpy as np


# In[421]:


with open('iris_train.tsv', "r") as f: 
    for line in f: 
        #print(line)
        s_list11=[]
        s_list2=[]
        s= f.readlines()
        for line in range(len(s)): 
            #print(line)
            s_list11.append(s[line].strip().split('\t')[:2]) # This command returns a list of lists. each list is a 2 length string containing the petal width and length of the training data 
            s_list2.append(s[line].strip().split('\t')[-1])  # s_list2 is a list of strings containing the y label data
        #print(s_list2)
        #print(s_list11)


# In[422]:


with open('iris_test.tsv', "r") as f1: 
    for line in f1: 
        #print(line)
        s_list1=[]
        s1= f1.readlines()
        for line in range(len(s1)): 
            #print(line)
            s_list1.append(s1[line].strip().split('\t'))  #s_list1 is a list of lists. each list is a two length string containing petal width and length information of the test data 
x_test=s_list1
X_Test=[]
for line in x_test:
    X_Test.append([float(i) for i in line])  # Need to do this to convert the numbers from strings to floats for subsequent analysis 
print(X_Test)


# In[423]:


x_train=s_list11
X_Train=[]
for line in x_train:
    X_Train.append([float(i) for i in line])  # converts all the X_train data from strings to floats for subsequent analysis 
print(X_Train)


# In[424]:


y_train= s_list2
print(y_train)


# In[ ]:


Write a function knn_train(m, x_train, y_train) where m is some appropriate 
# data structure for the knn model, and where x is the training data explanatory 
# variables and y is the training data labels. 
# m is passed by reference and should be modified to store x_train and y_train in m.


# In[425]:


m=[[],[]]  # an empty list of two empty lists which is later modified to contain the x_train and y_train data 
def knn_train(m, X_Train, y_train):
    """" This function takes in an list of two empty lists called m, and two lists. X_Train is a list of lists containing the petal length and petal width
    y_train is a list of strings which has the corresponding labels for the X_Train lists. This function modifies m and returns the 
    empty list as two lists of lists: first list is the X_Train values, second list is the Y_labels for it"""
    m[0].append(X_Train)  
    m[1].append(y_train)
    return m


# In[426]:


knn_train(m,X_Train,y_train)


# In[427]:


X_Test


# In[428]:


len(X_Test)


# In[429]:


m[0][0]


# In[ ]:


(3) Write a function knn_predict(m, x_test) where x_test is a sequence of 
# explanatory variables, which returns a sequence of predictions, 
# one for each row of data.


# In[387]:


m[1][0][14]


# In[317]:


X_Test


# In[308]:


len(m[0][0])


# In[443]:


def knn_predict(m, X_Test):
    """This function takes in as parameters the taining dataset m and the test dataset X_Test. The fist list in m is the list 
    of the vectors (petal length and petal width). The X_Test contains the vectors for the flowers whose species we need to determine.
    I will use the distance_euc function from above to calculate the distance between each vector of the X_Test, and the vectors
    of the training dataset. After this, for each of the 15 distances calculated for the 5 points of the data set, I will 
    find the minimum value. I will then choose the Y label from the second list of my dataset for the corresponsing X_vector 
    values. This will be the prediction of the particular row of the X_Test vector"""
    import numpy as np
    labels=[]   #  this is the list which will contain all the predictions at the end 
    for i in range(len(X_Test)): # which is 5 
        distance=[]
        for b in range(len(m[0][0])): # which is 15 
            distance.append(distance_euc(X_Test[i],m[0][0][b]))  # 15 distances for each of the five points 
            smallest_value= np.min(distance)   # for each of the 15 distances this gives the smallest euclidean distance value 
        index=np.where(distance==smallest_value)[0][0]  # find the index of the y label for the corresponding x_train vallues which gave the smallest euclidean distance 
        labels.append(m[1][0][index])   # append the y labels for the smallest euclidean distance vector from the training data
            
    return labels


# In[444]:


knn_predict(m, X_Test) #Test this on the data to check if the outputs are returned


# In[432]:


X_Test


# In[346]:


# (4) Define the data structure for your model and use these functions to train 
# the model on the data in "iris_train.tsv", then predict the labels for the 
# test data in "iris_test.tsv" and print them.


# In[445]:


#Defining my data structures: 
# m is a list of two lists. This is the training dataset. The first list is a list of vectors. The vectors represent the x and 
#y coordinates of the trainind data: they represent the length and width of the columns. The second list of m is the y labels 
# of the trainid data 
m


# In[435]:


#Defining my data structures: 
#X_Test represents my test set. Each list is a list of two float points, representing the petal length and petal width 
X_Test 


# In[439]:


#Defining my data structures: 
#X_Train is a list of lists. Each list is a vector: length and width of petals of the training data 
X_Train


# In[442]:


#Defining my data structures
#y_train is a list of the corresponding y labels.
y_train 


# In[ ]:




