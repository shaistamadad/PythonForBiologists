#!/usr/bin/env python
# coding: utf-8

# In[41]:


cd Downloads


# In[42]:


import Bio
from Bio import Blast 
from Bio.Blast import NCBIXML


# In[45]:


# the following code will extract drosophila and celegans proteins (in two separate lists) from the drosophila_celegans. xml BLAST output. 
handle1 = open('drosophila_celegans.xml')

drosophila_celegans_match = [[],[]]  # created an empty list of two empty lists. The first empty list will be filled with the drosophila protein matches, and the second list will be filled with the celegan protein matches from the drosophila to celegans Blast ouput 
THRESHOLD_VALUE_E = 1e-20   # this e-value threshold will be used later to extract only those alignments for which the e value is less than the e-threshold 
blast_record= NCBIXML.parse(handle1) 
for record in blast_record:   # a for loop iterating over all the matches in the parsed drosophila_celegans.xmlfile 
    for alignment in record.alignments: 
        filter_threshold= False   # Using filter_threshold as a flag. When this is set to True, it will help extract high scoring pairs with e-values smaller than the threshold e-value
        for hsp in alignment.hsps:
            if hsp.expect <THRESHOLD_VALUE_E:
                filter_threshold = True    
                
        if filter_threshold == True:  #a conditional statement to fill the two lists of  drosophila_celegans_match with query(drosophila) and target(celegans) proteins only for hits with e_values below the threshold value 
            drosophila_celegans_match[0].append(record.query)    # drosophila_celegans_match[0] refers to the first list 
            drosophila_celegans_match[1].append(alignment.title)  # drosophila_celegans_match[1] refers to the second list 
print(len(drosophila_celegans_match[0]))
    


# In[46]:


print(len(drosophila_celegans_match[1]))


# In[47]:


(len(drosophila_celegans_match[1]))


# In[48]:


# Same code as above, but this time for the 'celegans(query) and drosophila(target) blast output 

handle2 = open('celegans_drosophila.xml')

celegans_drosophila_match = [[],[]]  # created an empty list of two empty lists. These lists will be filled with the the best hits from the drophila to celegans Blast output. 
THRESHOLD_VALUE_E = 1e-20   # 
blast_record1= NCBIXML.parse(handle2) # use the parse command to parse the BLAST xml output and extract the information we need in the subsequent code 
for record1 in blast_record1:   
    for alignment1 in record1.alignments: # a for loop to iterate over all the alignments in the BLAST output 
        filter_threshold= False   # 
        for hsp in alignment1.hsps:  # hsp refers to the highest-scoring segement pair: a local alignment with one of the highest alignment scores in a given search 
            if hsp.expect <THRESHOLD_VALUE_E:   # hsp.expect is the e-value for the hsp. The lower the hsp.expect, the more significant the finding 
                filter_threshold = True   # 
                
        if filter_threshold == True:  # Using this Boolean means the following code is executed only in cases where the e_value for a given hsp in the alignments is lower than the threshold value 
            celegans_drosophila_match[0].append(record1.query)   # list of all the celegans proteins from the celegans to drosphila blast 
            celegans_drosophila_match[1].append(alignment1.title)  # list of all the drosophila proteins 
print(len(celegans_drosophila_match[0]))


# In[49]:


len(celegans_drosophila_match[1])


# In[59]:


def get_reciprocal_best_hits(A_to_B, B_to_A, homologous_pair= True):
    """ this function carries out reciprocal best blast hits. The parameter A_to_B represents the output of a forward A to B Blast. A_to_B contains two lists: first list has protein sequences from the query sequence
    and the second list contains the protein sequence matches from the target sequence. 
    Parameter B_to_A represents the output from a reverse blast: where now B is the query sequence and A is the target sequence against which 
    the query sequence is aligned. 
    when the flag homologous_pair == True, this function will carry out reciprocal blast hits: it will give only the A to B matches for which B to A 
    matches were found. 
    If the flag homologous pair== False, this function will give as output a dataframe with the A to B matches and the B to A matches"""
    match_list = [[],[]]  # an empty list of two empty lists. This first empty list will be filled with protein matches from one species and the second list will be filled with protein matches from the other species 
    if homologous_pair== True:  # the following is the code to carry out essentially an intersection: get only the matches which are present in A_to_B and B_to_A
        #match_list = [[],[]]
        for i in range(0, len(A_to_B[0])):
            for j in range(0, len(B_to_A[0])):
                if A_to_B[0][i]== B_to_A[1][j] and A_to_B[1][i]== B_to_A[0][j]:   #  A_to_B[0][i] and B_to_A[1][j] are two lists which contain proteins from the same species and they are the query and target sequences in A_to_B and B_to_A blast outputs respectively 
                    match_list[0].append(A_to_B[0][i])  # the first list of match list now has all the protein sequence matches from one species 
                    match_list[1].append(A_to_B[1][i]) # the second list of match_list now contains all the protein sequences from the second species
    else:  # if the homologous_pair flag is set to False when calling out this function, the function will run this code to get a list which contains the A to B matches as well as the B to A matches 
        AB_BA_Union= A_to_B   # the AB_BA_Union contains two lists with A and proteins from the forward blast 
        AB_BA_Union[0].extend(B_to_A[1]) # Add the B to A reverse blast protein matches from one species. In the case of the celegans and drosophila blast output, this amounts to around 71000
        AB_BA_Union[1].extend(B_to_A[0])  # AB_BA_Union[1] and (B_to_A[0] contain proteins from the same species 
        for i in range(0, len(AB_BA_Union[0])):   
            if i==0:
                match_list[0].append(AB_BA_Union[0][i])   # the union of protein matches is the Sum of  A to B matches and B to A matches - A intersection B matches. So,need to substract the results from the reciprocal blast hits to get the correct answer 
                match_list[1].append(AB_BA_Union[1][i])
            else:
                Intersection= False   
                for j in range(0,len(match_list[0])):
                    if match_list[0][j]== AB_BA_Union[0][i] and match_list[1][j]== AB_BA_Union[1][i]:  # condition of A intersection B 
                        Intersection= True  # when A intersection B happends, the Boolean is equal to True
                if not Intersection: # when Intersection is not true, the following code is run. so all the intersection= True cases will be ignored 
                    match_list[0].append(AB_BA_Union[0][i])
                    match_list[1].append(AB_BA_Union[1][i])
                    #print(len(match_list[1]))
   
    A= match_list[0]
    B= match_list[1]
    import pandas as pd
    data = pd.DataFrame({"Drosophila": A, 'Celegans': B})   # Generates a dataframe with two columns. The first column contains all the protein sequences from Drosophilam the the second column contains all the protein matches from celegans 
    return data


# In[60]:


get_reciprocal_best_hits(drosophila_celegans_match,celegans_drosophila_match,homologous_pair= True)  # calling the function on the two xml files with homologous_pair= True will give the results of the reciprocal best blast hits 


# In[61]:


D= get_reciprocal_best_hits(drosophila_celegans_match,celegans_drosophila_match,homologous_pair= True)


# In[63]:


D  # D is a dataframe with proteins from Drosophila in the first column and proteins from Celegans in the second 


# In[64]:


# A text file Orthologs_sm8847_1.txt is generated,Each line of the text file includes one drosophila and celegan match. 
   # the first protein is always a protein from Drophila and the second is a protein from Celegans
D.to_csv(r'C:\Users\admin\Orthologs_sm8847_1.txt', header=True, index=True, sep=' ', mode='a')


# In[65]:


# When the  get_reciprocal_best_hits function is calles with homologous_pair= False, the output is HSPs from species A to B or B to A 

Non_homologous_matches= get_reciprocal_best_hits(drosophila_celegans_match,celegans_drosophila_match,homologous_pair= False)


# In[66]:


Non_homologous_matches


# In[67]:


# For Part 2: text file with matches from A to B or B to A.
Non_homologous_matches.to_csv(r'C:\Users\admin\Orthologs_sm8847_1_FALSE.txt', header=True, index=True, sep=' ', mode='a')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




