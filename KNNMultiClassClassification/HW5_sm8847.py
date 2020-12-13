#!/usr/bin/env python
# coding: utf-8

# In[32]:


import sys

if len(sys.argv) !=2:
    print("Usage: python HW5.py cv")
    sys.exit(1)
d= int(sys.argv[1])   #sys.argv[1] is an string but d is an integer. Without converting d into an integer, can put the integer cv value on the commandline 


# In[45]:


# The data consist of microarrays from 89 different individuals with acute lymphoblastic leukemia (ALL)
# There are three subgroups of the data including B-cell tumours with BRC/ABL mutation 
# and those ALL samples with no cytogenic abnormalities (NEG), 
# and ALL1/AF4 show a translocation between chromosomes 4 and 11 etc.
import numpy as np
import pandas as pd
from sklearn import neighbors, datasets
#from sklearn.model_selection import train_test_split
#from sklearn.model_selection import cross_val_score

def cross_val_score_solution(clf, gene_exp, tissue_type, cv=10):
    """"This function takes in four parameters and returns a cross-validation estimation of accuracy of our model in predicting 
    the y_labels of our test data. The parameter gene_exp is a numpy array(89 rows by 2147 columns in the given example but this function will work for any array), where each row represents data from 89 different individuals. Each column in this array represents
    gene expression data for a given gene (2146 in our given example). This function will first convert this data into a dataframe.
    A cross validation requires the data to be divided into equal parts. The parameter cv will determine how many parts the
    data will be divided into.  A for loop will run the cross_validation cv times. Each time, one part will be treated as 
    the test set, the rest of the data will be concatenated and treated as the training data. For both the  training data and 
    the test data, the data will be divided into the X_training data(containing only the gene expression data) and the Y_labels. The parameter clf represents the knn
    algorithm. """
    dataset = np.column_stack([gene_exp, tissue_type])  # add the tissue_type data to each row of the gene_exp data. We get an 89 by 2147 array now 
    dataframe22=pd.DataFrame(dataset) #convert the dataset from an array type into a dataframe 
    dataframe22.sample(frac=1)  # shuffle the rows of the dataframes once to control for any trends in data which might affect the accuracy scores 
    folds = np.array_split(dataframe22, cv)  # split the dataframe into cv equal parts. fold is a list of dataframes 
    c= np.array([])  # this empty array will contain all the accuracy scores from the k-fold cross_validation: the number of accuracy scores will be equal to cv 
    for i in range(cv):  # start a for loop to do cross_validation 
        train = list(folds) #create a copy of folds so the original folds is not changed 
        test = folds[i]   # each dataframe in the list of dataframes will be the test dataset once. 
        Y_Test= test.iloc[:,-1]  # Extracting only the last column as the Y label for the test data 
        X_Test=  test.iloc[:,:-1]  # extracting all the columns of the dataframe but the last one. This is the gene_expression data of the test dataset. we  need this data for the clf.score function later. 
        del train[i]     # need to delete the test dataframe from the original list of dataframes to get the training data 
        train = pd.concat(train)  #after deleting the test dataframe, join the rest of the dataframes into one dataframe 
        Y_Train= train.iloc[:,-1]  # Y_Train is the Y labels of the training data: all the labels of the ALL cancer subtypes
        X_Train= train.iloc[:,:-1]  #X_Train contains only the X_training data: e.g., the gene expression data without the labels   
        clf.fit(X_Train, Y_Train)  # using the clf.fit algorithm to develop a prediction model using our training data.
        All_scores= clf.score(X_Test, Y_Test)  # using the clf.scores function to test our model's accuracy in predicing the y_label for the test data based on the model developed using the training data. The accuracy is based on comparing the predicted y_label for the test data based on our model, compared with the actual truth which we know. 
        c= np.append(c, clf.score(X_Test, Y_Test))  #the empty array c is now appended with the accuracy scores for the all the clf.score calculations done for each dataframe in the list of dataframes called fold .Number of accuracy scores is  dependent on the value of cv 
    average_accuracy= c.sum()/cv  # we get the average accuracy of our model in predicting the y_label by getting a mean of the accuracy scores 
    
    return average_accuracy

n_neighbors = 15  
clf = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')  # neighbour is a learning method provided by sklearn to train our model.KNeighboursCLassifier method is used as our Y_labels are categorical data type. 
#The principle behind nearest neighbor methods is to find a predefined number of training samples closest in distance to the new point, and predict the label from these
#We have defined the number of samples to be 15.  Setting the weights= uniform means all points in the neighbourhood are weighted equally, and their distance from the test point is not considered 
gene_exp = pd.read_csv("gene_expr.csv", header=None).values
tissue_type = pd.read_csv("gene_labels.csv", header=None).values
gene_exp = np.transpose(gene_exp)  # reverses the order of the rows and columns in the array (2146 by 89 to 89 by 2146)
tissue_type = np.ravel(tissue_type)  # the data has been converted into a one dimensional array

# incorrect- testing on training set. Wrong!!!!!
#clf.fit(gene_exp, tissue_type)
#print("Wrong accuracy: %0.2f" % clf.score(gene_exp, tissue_type))

# we use an independent test set. Correct!!!!!!!!!
#X_train, X_test, y_train, y_test = train_test_split(gene_exp, tissue_type, test_size=0.3, random_state=0)
#clf.fit(X_train, y_train)
#print("Independ. set accuracy: %0.2f" % clf.score(X_test, y_test))
      
# cv- also correct!!!!!!!
# TODO: your cross-validation function should return the mean accuracy
print("Average accuracy for", d, " K-Fold Cross_ Validation is", cross_val_score_solution(clf, gene_exp, tissue_type, cv=d))
#print("CV accuracy: %0.2f" % (mean_accuracy))


# In[44]:


cross_val_score_solution(clf, gene_exp, tissue_type, cv=10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




