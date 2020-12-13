#!/usr/bin/env python
# coding: utf-8

# In[91]:


#Question 1: 

def median(list): 
    """function median takes in a list of numbers, and returns the median
    the list will first be sorted in ascencing order. An assert statement will block the code if the length of
    the list is an even number. In order to find the median, we will locate the element of the list at the n+1/2-1 position
    The -1 because a list indexes from 0"""
    assert (len(list))%2 != 0, "The median function only works in list for odd length" # this assert statement says that if the length of the list is divided by two, and the remainder is not equal to zero, this means that the length is an even number 
    new_list= list.copy() # I will make a copy of the original list for use in the next step. This is to make sure that the original argument is not modified 
    sorted_list= new_list.sort()
    n= len(new_list) # we will use the n value to find the central element  of the list 
    number= (n+1)/2  # this gives a decimal point answer
    number2= int(number)  # to convert the answer to an integer as the index value needs to be an integer
    number3= number2-1  # I substracted 1 from number 2 as the list indexing starts from 0
    median= new_list[number3]
    return median     


# In[90]:


median(Control)


# In[59]:


Stressed = [8.640702, 10.563801, 10.112522, 10.382829, 10.017666]
Control = [11.793648, 10.933091, 10.631650, 11.129426, 9.739313]


# In[77]:


Stressed[0:5]


# In[64]:


Stressed.extend(Control)


# In[66]:


print(Stressed.extend(Control))


# In[43]:


from random import shuffle 


# In[44]:


help(shuffle)


# In[ ]:





# In[98]:


# Question 2

def permtest(listone, listtwo): 
    """ This function takes in two lists, uses the median function above to calculate their  medians and finds the difference
    listone and listwo are the parameters of the function. They are lists of numbers, and we are interested in finding the difference 
    in the median of these functions. 
    I will use the median from the previous question to find the medians of listone and listtwo"""
    list1= listone.copy()
    list2= listtwo.copy() # I will use these two lists in the arguments so that the original arguments are not modified 
    median1= median(list1) # calling the function from part 1 
    median2= median(list2)
    difference1= median2-median1  # the difference of the median of the two lists has been calculated 
    
    list1.extend(list2)  # note that the list1 has now been modified. When we use list1 subsequently, it will now be a 10 element list containing elements of list1 and list2
    n=0  # to 
    for i in range(1000): 
        from random import shuffle # import the shuffle function from the random module to shuffle the elements of the modified list 1
        shuffle(list1, random= None)
        n= len(list1) 
        number= (n)/2  # assuming that length of list 1 is even, given it is an extension of list1 and list2
        number2= int(number)# this needs to be an integer as we can't use a float to index a list
        shuffledlist1= list1[0:number2] # I will now create two new five element lists from the modified list1. the first list includes half of the total elements of the modified list1.
        shuffledlist2= list1[number2:]  # this will generated a second five element list after shuffling list 
        difference2= median(shuffledlist1)-median(shuffledlist2) # this computes the difference of the medians of the two new lists created after shuffling the modified list1
        if  difference2 <= difference1:
            n+=1       # n represents the numbers of instances when the difference of the median of the post-shuffled lists  is less than or equal to the difference of our orginal  difference of the medians of the lists from our argyment 
    fraction= n/1000   # This will give as a fraction the number of times the medians of the 1000 iterations was less than the difference of the medians of the orgininal two lists 
    return fraction


# In[99]:


permtest(Stressed,Control)


# In[72]:





# In[ ]:




