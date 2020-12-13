#!/usr/bin/env python
# coding: utf-8

# In[108]:


cd Downloads


# In[42]:


import Bio
from Bio import Blast 
from Bio.Blast import NCBIXML


# In[ ]:


# Last Question of The Assignment: Use a different data structure to solve the problem 

# Instead of using a list, I have used dictionaries in the alternative solution to the problem, using a different data structure 


# In[127]:


handle1 = open('drosophila_celegans.xml')

drosophila_celegans_match = {}   # this empty dictionary will be filled with key and values, where key= drosophila protein, value= celegans protein 
THRESHOLD_VALUE_E = 1e-20   # this e-value threshold will be used later to extract only those alignments for which the e value is less than the e-threshold 
blast_record= NCBIXML.parse(handle1) # use the parse command to extract information from the xml file 
for record in blast_record:   
    for alignment in record.alignments: # a nested loop for all the alignments within a given --- 
        filter_threshold= False   # Using filter_threshold as a flag. When it is 
        for hsp in alignment.hsps:
            if hsp.expect <THRESHOLD_VALUE_E:
                filter_threshold = True
                
        if filter_threshold == True: # for all the hsps with an e_value below the threshold value,  drosophila_celegans_match will be updated to add drosophila and celegans proteins as key and values respectively 
            drosophila_celegans_match.update({record.query: alignment.title})  
print(len(drosophila_celegans_match))


# In[192]:


len(drosophila_celegans_match)


# In[153]:


type(drosophila_celegans_match)


# In[124]:


# The same code, this time run to get a dictionary in which key is celegans is the key and the corresponding drosophola protein the value 

handle2 = open('celegans_drosophila.xml')

celegans_drosophila_match = {} #
THRESHOLD_VALUE_E = 1e-20  # this e-value threshold will be used later to extract only those alignments for which the e value is less than the e-threshold 
blast_record1= NCBIXML.parse(handle2) # use the parse command to extract information from the xml file 
for record1 in blast_record1:   
    for alignment1 in record1.alignments: 
        filter_threshold= False   
        for hsp in alignment1.hsps:
            if hsp.expect <THRESHOLD_VALUE_E:
                filter_threshold = True
                
        if filter_threshold == True: 
            celegans_drosophila_match.update({record1.query: alignment1.title})
print(len(celegans_drosophila_match))


# In[128]:


type(celegans_drosophila_match)


# In[240]:


# In order to find reciprocal blast hits. 

match=[]
for i in drosophila_celegans_match.keys():
    for j in celegans_drosophila_match.keys():
        if i==celegans_drosophila_match[j]:  # the key of drosophila_celegans_match and the value of celegans_drosophila_match are both drosophila proteins
            if j==drosophila_celegans_match[i]:
                match.append([i,drosophila_celegans_match[i]])  # match is a list of lists. Each list contains one drosophila protein and the corresponding c-elegans protein 


# In[245]:


len(match)
match[1]


# In[159]:


# To write out a text file 
with open('Orthologs_sm8847_one.txt', 'w') as output_fh: #'Orthologs_sm8847_one.txt' will be created, ready to be written in 
        for ortholog_pair in match:  # a for loop to write each pair as a line separated by tab in the text file 
            output_fh.write(ortholog_pair[0] + "\t" + ortholog_pair[1]+"\n")


# In[224]:


# To get A_to_B or B_to_A pairs, Invert one of the dictionaries' keys and values, append them and remove any repeat key values 
Inverted= drosophila_celegans_match  # invert key to value assignment of drosophila_celegans_match
inverted_dict = dict([[v,k] for k,v in Inverted.items()])


# In[226]:


celegans_drosophila_match.update(inverted_dict)


# In[247]:


#(celegans_drosophila_match)  # this is the updated dictionary containing all the A to B and B to A matches as a dictionary


# In[236]:


# this dictionary can now be written into a csv file 
import csv

dict = celegans_drosophila_match
w = csv.writer(open("output.csv", "w"))  # outpyt.csv file will contain all the matches from A to B and B to A 
for key, val in dict.items():
    w.writerow([key, val])


# In[ ]:


# Comment on the computational complexity using the big O notation 

#The computational complexity of the original solution is higher, I used a greater number of functions, a longer code containing, hence a larger number of algorithms were run 
#more loops than the alternative version. The running time of this code is less than the originak solution. ALthough this 
# has some errors, which may have contributed to the smaller running time, nevertheless the overall structure of this code suggests a lower computational complexity 

