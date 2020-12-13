#!/usr/bin/env python
# coding: utf-8

# In[2]:


cd Downloads


# In[11]:


from seq_tools_sm8847_module import read_fasta 
import re
def display_restriction_sites(sequence):
    """This function takes in a sequence, reads it using the read_fasta fucntion from last week's assignment
    it then uses a regular expression to define a restriction sequence. 
    using the data drame and other statistical tools from panda, this function will then fill up a 4 by 7 frequency column
    with the distribution of nucleotides in all the sequences found in a given file of dna sequence 
    the parameter sequence: any fasta file that contains a single string of DNA. """ # find the hits
    sequence1 = read_fasta(sequence)
    recognition_sequence=r'[AG]GG[AGTC]CC[CT]'
    found = re.findall( recognition_sequence , sequence1 )
    from pandas import Series, DataFrame
    import numpy 
    s= Series(found) #convert the data type of found from a list to Series, which is a one-dimensional array for the next step 
    frequency_matrix = numpy.zeros((4, len(s[0])), dtype=numpy.int) # we create an empty array of 4 rows, each with 7 spots. Will fill this array by countinf the number of A,G,T and C nucleotides at each position for all the instances when the draII sequence has occured
    base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3} # we have created a dictionary, where the A, C, G and T will be represented by row 1, 1, 2 and 3 respectively in the array 
    for sequence in s:  # a for loop iterating over all the individual incidences of the draII restriction site in a given DNA sequence 
        for index, base in enumerate(sequence): #Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
            frequency_matrix[base2index[base]][index] += 1  # for each restriction site found, all the nucleotides will be distributed across the four rows and the empty frequency table will be filled
    from pandas import Series, DataFrame
    Data=DataFrame.from_items([('A', frequency_matrix[0,]), ('C',frequency_matrix[1,] ), 
                     ('G',frequency_matrix[2,]), ('T',frequency_matrix[3,] )],
                     orient='index', columns=['one', 'two', 'three', 'four', 'five', 'six', 'seven'])
    Data_new = Data.loc[:,"one":"seven"].div(Data.sum( axis= 0,skipna=True))  # converts the frequency matrix into a position weight matrix by dividing each element of a column by the sum of that column 
    return Data_new


# In[12]:


c=display_restriction_sites("draII.fa")
c         
# Note that the sum of columns equals 4534 for all seven columns. This is important, as there were a total of 4534 incidences in the draII.fa file where the restriction sequence was found


# In[170]:


from Bio import Restriction 
Restriction.StyI
Restriction.StyI.site


# In[13]:


from seq_tools_sm8847_module import reverse_complement, get_translation 


# In[15]:


def restriction_site_scan(file_name): 
    """This function take in a fasta file, reads it. It then looks for a restriction sequence in the dn sequence of the file, 
    and replaces all instances of the sequence with NNNNNN in the DNA sequence, and in the reverse complement of the DNA sequence"
    for the DNA sequence and its reverse complement, this function also gives the indices of where the Styla restriction sequence was found 
    and the exact sequence of the restriction sequence (as there are more than on possible matches)
    file_name is the input we give to the function. It is any fasta file containing one DNA sequence"""
    import re  # need the re module for replacing the restriction sequence with our NNNNNN sequence 
    original_input= read_fasta(file_name)  # read the fasta file 
    reverse_comp_file= reverse_complement(original_input)  # generate the reverse complement using a function i wrote for last week's assignment 
    recognition_sequence= 'CC[AT][AT]GG' # using the IUPAC ambiguity code, where W represents A or T base nucleotide. CCWWGG is represented using a regular expression syntax. The[AT] means either A or T
    replace= 'NNNNNN'  # or '[ATGC]'*6?
    # store the match object in the variable m
    runs = re.finditer(r"CC[AT][AT]GG", original_input)  # this function will find all the instances of regualr expression in our target sequence 
    for match in runs:   # for each sequence found, I will find the indices using this for loop
        run_start = match.start()
        run_end = match.end()
        S= print("StyI sequence match in orginal sequence from " + str(run_start) + " to " + str(run_end))
        Y= print (match)
    runs2= re.finditer(r"CC[AT][AT]GG", reverse_comp_file) # the same sequence of events for the reverse complement 
    for match in runs2:
        run2_start = match.start()
        run2_end = match.end()
        S2= print("StyI sequence match in reverse complement of original sequence from " + str(run2_start) + " to " + str(run2_end))
        Y2= print (match)
    p = re.compile('CC[AT][AT]GG', re.VERBOSE)
    replaced_original= p.subn('NNNNNN', original_input)  # this function will replace all the regular expression instances with NNNNNN for the DNA sequence 
    replaced_complement= p.subn('NNNNNN', reverse_comp_file)  # same replacing operation for the reverse compliement 
    
    return replaced_original, replaced_complement, S, Y, S2, Y2


# In[16]:


restriction_site_scan("styI.fa")# this fuction finds all the indices for the instance of the regular expression in a dna sequence and its revrse compliement and replaces them with NNNNNN


# In[35]:



# PLease ignore everything below this cell. it is rough work. I didn't have time to delete it sorry 


Seq.IUPAC


# In[37]:


Seq.startswith   # Seq. and then press tab


# In[38]:


myseq= Seq(C)


# In[39]:


myseq


# In[42]:


myseq.alphabet


# In[43]:


from Bio.Alphabet import IUPAC


# In[44]:


myseq = Seq(C, IUPAC.unambiguous_dna)


# In[45]:


myseq.alphabet


# In[46]:


len(myseq)


# In[47]:


print(myseq[0])


# In[48]:


myseq.complement()


# In[50]:


from Bio.SeqRecord import SeqRecord


# In[52]:


simpleseqr = SeqRecord(myseq)
simpleseqr


# In[20]:


import re
p = re.compile('CC[AT][AT]GG', re.VERBOSE)
p.subn('(A|T|G|C)(A|T|G|C)(A|T|G|C)(A|T|G|C)(A|T|G|C)(A|T|G|C)', C)


# In[228]:


D= reverse_complement(C)
m2= re.search(('CC[AT][AT]GG'), D)
print(m2)
print(m2.group())


# In[210]:


len(D)


# In[45]:


runs = re.finditer(r"CC[AT][AT]GG", C)
for match in runs:
    run_start = match.start()
    run_end = match.end()
    print("StyI sequence match in orginal sequence from " + str(run_start) + " to " + str(run_end))
    print (match)


# In[240]:


runs = re.finditer(r"CC[AT][AT]GG", D)
for match in runs:
    run_start = match.start()
    run_end = match.end()
    print(match)
    print("StyI sequence match in reverse complement sequence starts from " + str(run_start) + " to " + str(run_end))


# In[238]:


C[1818:1824], C[1901:1907], 


# In[197]:


restriction_site


# In[175]:


Seq.Seq    
    


# In[181]:


A= ('AGCAAGCT')


# In[182]:


reverse_complement(A)


# In[186]:


b='[ATGC]'*6


# In[187]:


b


# In[220]:


'[ATGC]{6}'


# In[53]:


from scipy import stats


# In[54]:


stats


# In[ ]:




