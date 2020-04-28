# cc 11.1
'''
A = [1,6,9,11,13,None,None,None,None]
B = [2,5,10,12]

def mergeA_B(A,B):
    a_left = 0
    b_ptr = 0
    while(A[a_left] is not None):
        a_left += 1
    a_left -= 1
    a_right = len(A) - 1
    while (a_left >= 0):
        A[a_right] = A[a_left]
        a_left -= 1
        a_right -= 1
    a_left = 0
    a_right += 1
    while(b_ptr < len(B)):
        if (A[a_right] < B[b_ptr]):
            A[a_left] = A[a_right]
            a_right += 1
        else:
            A[a_left] = B[b_ptr]
            b_ptr += 1
        a_left += 1
    return A
print(mergeA_B(A,B))
'''

# cc 11.2

#[a,b,c]
# sort it alphabetically

# find a set such that you have all anagram
# creat new list for anagram


# back trackign similar to palindrome and then make to.
# num of occu

# list of strings. create a list of dictionary. Figure out which are the same. Another dictionary with index. key: dicionary val: list [index]


