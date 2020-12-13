#!/usr/bin/env python
# coding: utf-8

# In[28]:


def read_fasta(fn):
    """ read_fasta is the name of a function which will take in a Fasta file as an input and return a string of the DNA sequence in the file. 
    The parameter (fn) is the name of the fasta file which we want our function to read. 
    This function has 4 nested functions within it, which come together at the end to help read the file"""

    def string_to_list_by_nl(s):
        """ string_to_list_by_nl function will convert a string separated by new lines into a list a list
        the parameter s is the dna sequence which will be converted into a list of strings by the line"""
        list_string = s.split('\n') 
        return list_string 
    def get_seq_from_list(dd):    
        """"This function, given a list of lines in fasta format for a single sequence,will return the sequence data 
        as a string, but will exclude the text part of the Fasta file"""
        a= ''
        new_string = a.join(dd[1:])
        return new_string
    def process_list_of_seq(ss):
        """  This function, given a list of multiple sequences in fasta format, returns a list of sequence data only  """
        rl = []
        for i in ss:
            li= string_to_list_by_nl(i)
            rl.append(get_seq_from_list(li))
        return rl
    def get_seq_list_from_file(fn):
        with open (fn) as f:
            s = f.read()
            return s.split('>')[1:]
    ss= get_seq_list_from_file (fn)
    rl=process_list_of_seq(ss)
    return ''.join(rl)
# With this function, I wanted to get a single string  containing multiple DNA sequences, each sequences separated by a blank line. however, I wasn't able to figure out how to separate the different sequences into separate lines within a single string. I will use the read_FASTA3 function below instead 


# In[29]:


def read_FASTA3(filename):
    """ This function will take in a fasta file, and return a list of strings. Each string in the list represents an indivdual fasta 
    record inside the Fasta file. Each record is a DNA sequence of a gene coding for a protein. This function will remove the text parts of the 
    Fasta records, e.g. gi|343403856|ref|NM_053051.3| Hom. """ 
    with open(filename) as file:
        contents = file.read() # the read() command reads the fasta file
        entries = contents.split('>')[1:] # skips blank element (1st line starts with '>')
        partitioned_entries = [entry.partition('\n') for entry in entries]  #Partition the strings to separate the first line from the rest
        pairs = [(entry[0], entry[2]) for entry in partitioned_entries]
        pairs2 = [ (pair[1].replace('\n', '')) for pair in pairs]
    return pairs2

ReadFile1= read_FASTA3("multiple_nt_seqs.fa")
ReadFile2= read_FASTA3 ("one_nt_seq.fa")


# In[7]:


def reverse_complement(dna_sequence):
    """" the if and else statements will be used to convert A to T, T to A, G to C, and C to G in a given string;
    An assert statement will be used to block the code if a given string of DNA sequence contains letters other than G,C,A.T. 
    reverse_complement: function which checks each letter of a DNA sequence string, and generates a complement in reverse order;
    dna_sequence: a string of DNA on which our function will run. This string will not contain any small letters, or letters other than G,C,A and T"""
    
    assert len(dna_sequence)== dna_sequence.count('A') + dna_sequence.count('T') + dna_sequence.count('G') + dna_sequence.count('C'), "valid DNA sequence should contain 'A','T' 'G','C'only"
    # assert statement is a check to ensure only a valid DNA sequence is generated 
    
    output= ''    # an empty string called output is created, which will be filled as our conditional statements in the loop run through the DNA sequence
    
    dna_sequence2 = []
    for i in (dna_sequence):   # a loop is created which will apply the following conditional statements on all elements of our string
            if i == 'A':
                output += 'T'# the if and elif conditional statements will change all the A's,T's,G's,C's to T's,A's,C's,G's respectively 
                dna_sequence2.append(i)
            elif i == 'T':
                output += 'A'
            elif i == 'G':
                output += 'C'
            elif i == 'C':
                output+='G'
    return output[::-1] 
for i in range(len(ReadFile1)):  # We will need to use a for loop on our ReadFile1 to get a reverse compliment of all the DNA sequences
    DNA_seq = ReadFile1[i]
    A=reverse_complement(DNA_seq)
    print (A)
for i in range(len(ReadFile2)):
    DNA_seq = ReadFile2[i]
    B=reverse_complement(DNA_seq)
    print (B)


# In[30]:


def get_transcript(dna_sequence):
    """" this function is essentially similar to the reverse_complement function. The difference is that the only change in a sequence
    will be to switch from T to U to get the mRNA. Note that mRNA has the same sequence as the coding strand DNA sequence for the 
    given protein. 
    the if and else statements will be used to convert A to A, T to U, C to C, and C to C in a given string;
    An assert statement will be used to block the code if a given string of DNA sequence contains letters other than G,C,A.T. 
    reverse_complement: function which checks each letter of a DNA sequence string, and generates a complement in reverse order;
    dna_sequence: a string of DNA on which our function will run. This string will not contain any small letters, or letters other than G,C,A and T"""
    
    assert len(dna_sequence)== dna_sequence.count('A') + dna_sequence.count('T') + dna_sequence.count('G') + dna_sequence.count('C'), "valid DNA sequence should contain 'A','T' 'G','C'only"
    # assert statement is a check to ensure only a valid DNA sequence is generated 
    
    output= ''    # an empty string called output is created, which will be filled as our conditional statements in the loop run through the DNA sequence
    
    for i in (dna_sequence):   # a loop is created which will apply the following conditional statements on all elements of our string
            if i == 'A':
                output += 'A'   # the if and elif conditional statements will change all the A's,T's,G's,C's to T's,A's,C's,G's respectively 
            elif i == 'T':
                output += 'U'
            elif i == 'G':
                output += 'G'
            elif i == 'C':
                output+='C'
    return output 
for i in range(len(ReadFile1)):
    DNA_seq = ReadFile1[i]
    C=get_transcript(DNA_seq)
    print (C)
for i in range(len(ReadFile2)):
    DNA_seq = ReadFile2[i]
    E=get_transcript(DNA_seq)
    print (E)


# In[31]:


def get_translation(sequence,reverse_complement_flag=False):
    """this function takes in a DNA or RNA sequence, and returns the list of amino acids of that sequence. The parameter 
    sequence is the DNA or RNA sequence to be translated. The parameter reverse_complement_flag if turned to yes will 
    obtain the reverse complement of the DNA or RNA sequence, and this will mean the translated protein is created from the 
    reverse complement of the sequence we entered. A RNA and DNA codon dictinary will be used to replace 3 nucleotides at a time with
    the corresponding value in the RNA and DNA codon table"""
    if reverse_complement_flag==True:  
        sequence=reverse_complement (sequence)
    else: 
        pass
    seq=sequence.upper()
    a=list(seq)
    DNARNA=["A","T","C","U","G"] 
    if set(a)<=set(DNARNA):
        print("true")
    else:
        print("false")  # This works as an assertion statement to catch any bugs in our file. The input file should be a DNA ior RNA file only. Otherwise this statement will say false  
        
       
    dna_rna_codon_table = {   # this DNA_RNA table has been copied from the internet. I have used the notation of using a single letter for each amino acid rather than the 3-letter name
        "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
           "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
           "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
           "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
           "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
           "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
           "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "UAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "UAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
           "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "UGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G",
           'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
           'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
           'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
           'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
           'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
           'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
           'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
           'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
           'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
           'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
           'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
           'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
           'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
           'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
           'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 
           'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    } 
    protein ="" 
    #if len(seq)%3 == 0:  #triplet nucleotide called the codon forms a single amino acid, so we check if the altered DNA sequence is divisible by 3
    for i in range(0, 3*(len(seq)//3), 3): #translation loop reads the DNA sequence three nucleotides at a time. 3*(len(seq)//3) to ignore the 1 or two nucleotides left at the end in case a sequence is not a multiple of 3
        codon = seq[i:i + 3] # loop will take a  DNA sequences codon from 0 to the size of the DNA sequence in steps of 3
        protein+= dna_rna_codon_table[codon]    #using the dictionary to convert the codon in triplet in nucleotide to amino acid in a single letter format
    
    return protein 
for i in range(len(ReadFile1)):
    DNARNA_seq = ReadFile1[i]
    print ("The amino acid sequence of one of the two sequences from multiple_nt_seqs.fa is", get_translation(DNARNA_seq,False)) 
for i in range(len(ReadFile2)):
    DNARNA_seq = ReadFile2[i]
    print ("The amino acid sequence of the  sequence from one_nt_seqs.fa is", get_translation(DNARNA_seq,False))


# In[19]:


def test_function(sequence): 
    """ the test function will take in a sequence of DNA, and give a reverse complement, RNA transcript and translation for the 
    sequence respectively. If the sequence is not a DNA sequence, we should get an assertion error"""
    a= print (reverse_complement(sequence))
    b= print (get_transcript(sequence))
    c= print (get_translation (sequence))
    return a,b,c


# In[32]:


test_function('ATATTGTAC')  # this is a test function to see if the functions we have created above work on any random DNA sequence


# In[21]:


test_function('ATATDSTAV') # Gives an assertion error as expected


# In[33]:


functions=[reverse_complement,get_transcript, get_translation]
arguments=['TTTASSSGCATCTTGC' ]
for i in range(len(arguments)):
    seq = arguments[i]
    a= print (reverse_complement(seq))
    b= print (get_transcript(seq))
    c= print (get_translation (seq))


# In[23]:


Trans1=get_translation('ATATTGTAC')


# In[24]:


c=get_transcript('ATATTGTAC')
c


# In[26]:


Trans2=get_translation(c)


# In[27]:


if Trans1==Trans2:
    print ("The translation function works on DNA and its mRNA sequence to give the same sequence of amino acids")


# In[ ]:





# In[ ]:




