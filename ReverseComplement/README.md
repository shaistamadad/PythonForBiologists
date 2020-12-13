Questions
A. Reverse Complement
1. Write functions
Using only basic python data types, e.g. list, tuple, or dict, write two different
functions that return the reverse complement (string) of an input (string) DNA
sequence. Each of these two functions, must solve the problem in a different way, i.e.,
use different data structures, control statements, and loops. Document each method
with a docstring which explains the approach you took. You can add a docstring by
using the a triple double-quote (""") string at the beginning of the function
definition. Make sure to give each function an intuitive name.
* Note that "way" refers mainly to which data structures are used and how you are completing the
process. Alternate functions which are not significantly different will not be counted. DO NOT ask the
instructors or teaching assistant about this distinction, if you think your function is too similar to
another one you wrote, it probably is.
Hint: try doing this using string methods, dictionaries, and/or lists, etc.
2. Test your functions on the sequence below, and print the output. (which is a 5'–3'
DNA sequence)
dna_sequence =
"ATGGAATGTTGTCCAAGATGAATAGTTTGTCATGATGCCCGTCGGGCAGATGGAGGACGGAGCTGAAGCCGCCGGGC
CCGCAGCAAACTTCGTCTAGACAGCCATGGCCTGTAAAGGTAGGGATATGCGCTTAG"
3. Self critique
For each function, consider:
o readability — is it easy to understand what it is doing?
o robustness — are there any inputs which may cause problems?
o correctness — are there any cases where the wrong answer will be produced,
even with correct input?
Write your summary of each method in comments preceding the function. Also make
sure to comment each small "section" of code and separate if from other lines with
new lines (empty lines). Don't stress over including a perfect analysis, it should be
straightforward to write your critique. For the record, you WILL be graded based on
your comments and code readability. I recommend writing comments for each step in
your method BEFORE you begin writing Python syntax. There should be a comment
for every process that you would explain if asked to verbally describe the function.
B. Tuples (5 Points)
1. Create a tuple tuple_1 containing the following: Met, 443, Ser, Arg, 567.5, Lys, Glu,
787, 8768, Val, Glu, Pro, Tyr, 57, Ser, His
2. Add the following strings to tuple_1 and name the new tuple as tuple_2: Pro, Lys,
Gln, Thr, Val, Glu, Cys, Ala, Glu
3. Determine whether tuple_2 has the same number of Glu and Val.
4. Determine whether Thr is present in tuple_2
5. Convert the following list to tuple named tuple_3
list = ["convert", "this", "list", "to", "a", "tuple"]

6. In tuple_3 determine the position of the word “list”
7. In tuple_3 try to replace the word “convert” with “not converted” and justify your
findings with suitable comments.

On the subject of iterating, what does the map function do? Include a short explanation in a
comment, and use it correctly in one of your homework questions.
A closely related function of map is reduce, what does it do? (no points)
Note: This is not a separate section! You have to use it in one of the other homework questions if you want the
point.
