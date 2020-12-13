#!/usr/bin/env python
# coding: utf-8

# In[79]:


#Question 1 
def count_base_sequence(base_sequence):
   '''args: base_sequence represents the sequence of DNA nucleotides, which are A,G,C,T. 
   the function count_base-sequence enumerates the number of these nucleotides in a given string'''
   return len(base_sequence)


# In[80]:


coreseq="ATGTACCACATAGTGATGGAGACGGAGCCATTGAAGCCGCCGGGCCCGCAGCAAACCTTCGGGGGGCGGCGGCGGCAACTCCACCGCGGCATTCGTTAG"


# In[81]:


count_base_sequence (coreseq)


# In[82]:


#let's test whether the defined function works on any random DNA sequence 
a = ("ATGC")


# In[83]:


count_base_sequence (a)


# In[84]:


#Question 2: Check whether the sequence ends in-frame (i.e. is the length a multiple of 3?) 
def validate_in_frame(nuc_seq):
    '''validate_in_frame checks if a given nucleotide sequence is a multiple of 3,
    nuc_seq is a string of nucleotide sequence'''
    if count_base_sequence(nuc_seq) % 3 == 0: 
        print ('given sequence ends in frame')
    else: 
        print ('given sequence does not end in frame')


# In[40]:


validate_in_frame(coreseq)


# In[41]:


randomseq= "ATGTACCACATAGTGATGG" # the sequence is assigned a name to make following operations easier to understand  


# In[42]:


validate_in_frame(randomseq)


# In[85]:


#question 3: Calculate the number of codons in the given sequence (assuming it is all translated)?

def number_codon (codon, constant):
    '''codon = count_base_sequence(base_sequence) where (base_sequence) is any random nucleotide sequence;
    codon divided by constant will give us the number of codons in this nucleotide sequence;
    constant is 3, as one codon requires three nucleotide bases'''
    return codon // 3    


# In[86]:


d= count_base_sequence(coreseq) # represents the first paramter (codon) in the defined function number_codon(codon,constant)


# In[87]:


print(d)


# In[89]:


number_codon(d,3) #gives the number of codons in our nucleotide sequence 


# In[90]:


#Question 4:check whether the given sequence starts with genetic code for methionine (ATG) 
coreseq.startswith("ATG")


# In[91]:


#Question 5: What is the GC content of this sequence? (fraction of G and C nucleotides) 

def det_GC_content (G_and_C, total_nuc):
    '''G_and_C= coreseq.count('G')+ coreseq.count('C')
    G_and_C is the sum of the G and C nucleotides in a given DNA sequence 
    total_nuc is the total number of nucleotides in a given DNA sequence i.e., total_nuc= count_base_sequence(coreseq)'''
    return (G_and_C/total_nuc)


# In[92]:


C= coreseq.count('G') + coreseq.count('C')


# In[93]:


print(C)


# In[94]:


D = count_base_sequence (coreseq)


# In[95]:


print(D)


# In[97]:


det_GC_content(C,D) #Gives the GC content in our DNA sequence as a decimal/float


# In[68]:


# Question 6: Write an assertion statement to check if the sequence is a valid DNA sequence

def validate_DNA_sequence (DNAseq2):
    return len(DNAseq2) == (DNAseq2.count('A') + DNAseq2.count('T') + DNAseq2.count('G') + DNAseq2.count('C'))
DNAseq2 = "ATGTACCACUUUAGTGATGGAGACGGAGCCATTGAAGUUUGGGCCCGCAGCAAACCTTCGGGGGGCGGCGGCGGCAACTCCACCGCGGCATTCGTTAG"
assert validate_DNA_sequence (DNAseq2),"DNA sequence must have only A,T,G,C"


# In[98]:


validate_DNA_sequence (coreseq) #This operation is testing the assertion above on our coreseq DNA sequence 


# In[99]:


validate_DNA_sequence ('ACGTaaaTTatGA')  # another example to check if the assetion statement spots lower case letters


# In[100]:


#Question 7: Write a function that converts height’s in cms to feet and use a docstring to document this function 

def convert_cm_feet(heights):
    ''' we use the 'for' iteration statement
    the parameter heights = list of 'heights expressed in cm; type of values: int;
    convert_cm_function will convert the unit of each element of the list from cm into feet'''
    b= [0.0328*i for i in heights]
    return b  


# In[101]:


Heights_in_cm= [235, 980, 560, 420, 150]


# In[102]:


print (Heights_in_cm)


# In[103]:


convert_cm_feet(Heights_in_cm)


# In[104]:


#let's try the coversion on a random list to see if it works for any random list 
S=[100,200,300,400,500,600]


# In[105]:


convert_cm_feet(S)


# In[ ]:




