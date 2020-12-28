
You will implement a simple version of a k-nearest neighbour predictive model for k=1

iris_train.tsv is a tab-separated file with training data to predict a species of iris. 

The first column is petal length in mm; the second column is petal width in mm; the third column is the species (there are two species).
Each row is data from a separate flower.

iris_test.tsv is an independent test set with petal length and width (flower species is not given).


(1) Write a function distance_euc(v1, v2) which computes the Euclidean distance  between two sequences 
(Euclidean distance is the sum of the squared element-wise differences).
   


(2) Write a function knn_train(m, x_train, y_train) where m is some appropriate  data structure for the knn model, and where x is the training data explanatory 
variables and y is the training data labels.  m is passed by reference and should be modified to store x_train and y_train in m.



(3) Write a function knn_predict(m, x_test) where x_test is a sequence of explanatory variables, which returns a sequence of predictions, 
 one for each row of data.



(4) Define the data structure for your model and use these functions to train  the model on the data in "iris_train.tsv", then predict the labels for the 
 test data in "iris_test.tsv" and print them.




(5) For 5 bonus points, write a user-defined type called "knn_class", using the above functions, which can be used in the following way: a = knn_class(x_train, y_train)
 pred = a.predict(x_test)


100 points total. You may use any builtin data type or numpy or pandas. 

Bonus points for good comments and use of assertions.

Upload your .py file and your .html file and .ipynb file if you used JupyterLab (named "quiz_knn_final_NETID.py", "quiz_knn_final_NETID.html", "quiz_knn_final_NETID.ipynb")

 Also upload a .txt file with your predictions for the test data  ("quiz_knn_final_NETID.txt").

Don't use additional modules beyond those mentioned above.

This is an open book exam and internet access to classes, python.org, numpy.org,scipy.org, pandas.pydata.org is allowed. 

Access to programming question and answer sites such as stack overflow is NOT allowed.

