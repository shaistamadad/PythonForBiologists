#!/usr/bin/env python
# coding: utf-8

# In[316]:


#Question 1. Function Number 1

##

def reverse_complement_function_1(dna_sequence):
    """" the if and else statements will be used to convert A to T, T to A, G to C, and C to G in a given string;
    An assert statement will be used to block the code if a given string of DNA sequence contains letters other than G,C,A.T. 
    reverse_complement_function_1: function which checks each letter of a DNA sequence string, and generates a complement in reverse order;
    dna_sequence: a string of DNA on which our function will run. This string will not contain any small letters, or letters other than G,C,A and T"""
    
    assert len(dna_sequence)== dna_sequence.count('A') + dna_sequence.count('T') + dna_sequence.count('G') + dna_sequence.count('C'), "valid DNA sequence should contain 'A','T' 'G','C'only"
    # assert statement is a check to ensure only a valid DNA sequence is generated 
    
    output= ''    # an empty string called output is created, which will be filled as our conditional statements in the loop run through the DNA sequence
    
    for i in (dna_sequence):   # a loop is created which will apply the following conditional statements on all elements of our string
            if i == 'A':
                output += 'T'   # the if and elif conditional statements will change all the A's,T's,G's,C's to T's,A's,C's,G's respectively 
            elif i == 'T':
                output += 'A'
            elif i == 'G':
                output += 'C'
            elif i == 'C':
                output+='G'
    return output[::-1]     # [::-1] will reverse the order of the elements of output to generate the reverse complement 


# In[321]:


reverse_complement_function_1("AtGC")   # testing our function on a random nucleotide sequence. Should give an assertion error since t is present


# In[359]:


#Self Critique Function 1: I have made attempt an attempt to make my function readible by adding docstring and comments wherever I felt there is a need. 
#In order to achieve robustness, I have added an assertion statement to stop my function from working on RNA sequences or sequences with small letters. T
#I have tested my function on a random sequences to see if they generate appropriate results for other sequences as well.


# In[318]:


dna_sequence="ATGGAATGTTGTCCAAGATGAATAGTTTGTCATGATGCCCGTCGGGCAGATGGAGGACGGAGCTGAAGCCGCCGGGCCCGCAGCAAACTTCGTCTAGACAGCCATGGCCTGTAAAGGTAGGGATATGCGCTTAG"


# In[322]:


dna_sequence   # let's test our function on the dna_sequence (Question 2) 


# In[325]:


reverse_complement_function_1(dna_sequence)


# In[343]:


# Function Number 2
# This function uses dictionary to assign values to keys. The keys are the nucleotides A,G,T,C in our given DNA sequence. The values are the nucleotides which will replace the key values in the DNA nucleotide sequence to generate the complement
# Whereas in function 1, a for loop was used with if and elif conditional statements, function 2 uses a list comprehension method instead.
#List Comprehensions are in-line for loops. Any iteration can be performed in a single line, hence they are an easier way of performing a loop.

def reverse_complement_function_2 (DNA_sequence):
    """This function uses dictionary to assign values to keys. The keys are the nucleotides A,G,T,C in our given DNA sequence.
    The values are the nucleotides which will replace the key values to generate the complement;
    the reverse sequence of complement will be generated using [::-1]
    this function will use a list comprehension method; DNA_sequence is any nucleotide sequence whose reverse complement we want to generate
    the while and else statement is working as alternate to an assertion statement: this function will work on a DNA sequence only if the bases are A, T, G or C only"""
    
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}  # argument of our function, which generates a library to use in the list comprehension
    
    while len(DNA_sequence)== DNA_sequence.count('A') + DNA_sequence.count('T') + DNA_sequence.count('G') + DNA_sequence.count('C'):   # makes sure function works on a valid DNA sequence only
        return ''.join([complement[base] for base in DNA_sequence[::-1]])
    else: 
        print ("this sequence is not a valid DNA sequence")


# In[360]:


#Self Critique Function 2: I have made attempt an attempt to make my function readible by adding docstring and comments wherever I felt there is a need. 
#In order to achieve robustness, I have added a while statement to stop my function from working on RNA sequences or sequences with small letters. T
#I have tested my function on a random sequences to see if they generate appropriate results for other sequences as well. 


# In[344]:


reverse_complement_function_2 (dna_sequence) #let's test our function on the dna_sequence (Question 2) 


# In[346]:


Randomseq= ("AtGV")
reverse_complement_function_2(Randomseq)     # let's test our function 2 on a random sequence to see if it works 


# In[347]:


if reverse_complement_function_1(dna_sequence)== reverse_complement_function_2(dna_sequence):
    print ("Both functions give a similar result")  
    # this is a test to see if both functions are giving the same reverse complement of our dna_sequence


# In[348]:


DNA_Test_Seq= ("ATGCTTGGCCAA")


# In[350]:


if reverse_complement_function_1(DNA_Test_Seq)== reverse_complement_function_2(DNA_Test_Seq):
    print ("two functions for generating DNA reverse complement created")
else: 
    print ('there is a problem in the execution of our two functions')
    
#this is to test if our functions work on any random DNA sequence


# In[351]:


# Part B: Tuples

#1: Create tuple_1. 

tuple_1= ('Met', '443', 'Ser', 'Arg', '567.5', 'Lys', 'Glu','787', '8768', 'Val', 'Glu', 'Pro', 'Tyr', '57', 'Ser', 'His')


# In[352]:


type(tuple_1)  # Just to check if I created a tuple or made a mistake. 


# In[247]:


#2: Add the following strings to tuple_1 and name the new tuple as tuple_2: Pro, Lys,Gln, Thr, Val, Glu, Cys, Ala, Glu

# First, let's create a tuple, say tuple11, which includes the given string converted into the tuple form


# In[353]:


tuple11= ('Pro', 'Lys','Gln', 'Thr', 'Val', 'Glu', 'Cys', 'Ala', 'Glu')


# In[248]:


type(tuple11)  # In order to check whether tuple1 is actually a tuple


# In[354]:


tuple_2= tuple_1 + tuple11  #note that tuple11 was created because we cannot add a string form to a tuple


# In[250]:


print(tuple_2)


# In[355]:


type(tuple_2)


# In[ ]:


#3: Determine whether tuple_2 has the same number of Glu and Val 


# In[356]:


#3: We will define a function, count_Glu_Val in order to answer this question. 

def count_Glu_Val (random_tuple):
    
    """ We use the 'if and else' conditional statement to check whether the number of "Glu" and the number of "Val" are equal;
    the function: count_Glu_Val, will give the answer: TRUE if number of Val=number of Glu, and FALSE if number of Val != no. of Val;
    random_tuple is a tuple containing the tuple of amino acids on which the function will operate"""
    
    if random_tuple.count('Glu')==random_tuple.count('Val'):
        print('TRUE')
    else:
        print ('FALSE')


# In[357]:


count_Glu_Val(tuple_2)  


# In[257]:


#The function gives the answer FALSE, which tells us that No of Val is not equal to No of Glu in tuple_2


# In[358]:


count_Glu_Val (Test_Tuple)   # to check if our function works on any random tuple. 


# In[264]:


#4: Determine whether Thr is present in tuple_2

# step 1: Let's create an empty string called c. 
c=''

# Step 2: let's use the for and if operations to create a loop which will check all the elements of tuple_2 to see if Thr is present

for i in tuple_2:
    if i=='Thr':
        print ("Contains Thr")


# In[285]:


#5: Convert the following list to tuple named tuple_3

list = ["convert", "this", "list", "to", "a", "tuple"] 


# In[ ]:





# In[286]:


tuple_3= tuple(list) # the tuple(list) operation converts a list into a tuple


# In[287]:


tuple_3


# In[289]:


#6: In tuple_3 determine the position of the word “list” 
tuple_3.index('list')  # note that indexing starts from 0 in tuples


# In[305]:


#7: In tuple_3 try to replace the word “convert” with “not converted” and justify your findings with suitable comments.
tuple_3['convert']= 'not converted'


# In[308]:


# as tuple_3 is immutable, i.e., we cannot make modifications such as replacements directly. We can modify tuple indirectly by using a function  

def modify_tuple(tuple_ran):
    """this function will be used to replace 'convert' with 'not converted' in the list which was converted to tuple_3. 
    Modify_tuple function will  modify the list and then convert the modified list to a new tuple
    tuple_ran is the tuple which we want to modify"""
    
    list[0]= 'not converted'   #first element of our list is replaced with 'not converted'
    
    print (list)   # to check whether we actually made the modification in our list 
    
    tuple_new= tuple(list) # the modified list is not converted into a tuple
    
    return (tuple_new) # note that the modified tuple has a new name, not tuple_3 because tuples are immutable. They cannot be modified


# In[309]:


modify(tuple_3)


# In[312]:


tuple_3   # tuple_3 is not changed, the function modifies the tuple to give a new tuple but this does not change the value set to tuple_3


# In[ ]:




