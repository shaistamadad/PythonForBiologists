In class quiz
Time limit: 1 hour.

You can use the internet to access NYU classes or the official python web site, but you
cannot do google searches or use stackoverflow or similar web sites.

Q. In this question you will implement what is called a permutation test in statistics.

Here are two vectors of data from an experiment that represent measurements of the (log)
expression of a certain gene from a stressed group and a control group of 5 mice each.

Stressed = [8.640702, 10.563801, 10.112522, 10.382829, 10.017666]

Control = [11.793648, 10.933091, 10.631650, 11.129426, 9.739313]

Write a function, median, that returns the median of a list of numbers (a median is the
middle value in a sorted list of the numbers). This function can assume that the arguments
have an odd number of elements- write an assertion that checks for this and aborts if not.
It should not modify the arguments passed to the function.

Write a function permtest that takes the two lists as arguments and:

(i) computes the difference of the median of the two lists (i.e. Stressed – Control) and saves
into a local variable.

(ii) repeats in a loop 1000 times the following:

Randomly assign the 10 data samples into two new lists of size 5 each and again
calculate the difference of medians. Record the number of iterations in which this shuffled
difference of medians is less than or equal to the original difference of medians from step (i).
(iii) finally, returns the fraction of the 1000 iterations in which the shuffled difference of
medians was less than or equal to the original difference of medians from step (i).

The permtest function should use your median function. It should not modify the arguments
passed to the function.

Test your function on the provided data and print the result.

Hint: look at the help for the shuffle function in the random module, and the sort method of
list.

Note that marks are given for good comments of the functions and the code. 
