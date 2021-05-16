'''
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]

in: A, B
ouput: T/False

pick two index i and j. and reverse it in B. to make A == B.

brute force:
    do all combinations of i and j and keep reversing


have i eveyrthing to left is matched and eveyrthing to right is not

question is can you just swap numbers

optimize less comparisons

store reverse strings?

rev_dict

is reverse diff swap

duplicate? store left and right arrays? or dictionarys?

as long as the arrays have same number of occurrnece then it's ok

1. take A and do num:occ dictionary
2. take B and see if you it equals dictionary

1. check length are ==
2. create dict num:occ
3. if you cannot subtract from dict then return False
'''
import collections
A = [1,2,2]

d = collections.Counter(A)

print(d[1])



