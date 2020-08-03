Need to find all of () in the string.


1. score is 1
2. two balanced next to each other
3. enclosed

assume cant have
((
))

(() (()))
i       j
recursion
1. i - start index
2. j - end index
return the score

state transition
# base case
if only two char and i and j are balanced: return 1
# recursive - string is larger than 2
if l == ( and r == ): 2*get_score(i+1,j-2)


must use a stack

res = 1

stack
if open add onto stack
if close pop the open off stack: add 1

1. find an opening and log distance of all opening to closing.
2. do smallest dist first

1. find all the end bracket pair


(() (()))