'''
# Optimal Utilization

[id,val]

sum a and b val is less then of equal to target
[a:id,b:id]

return ids


brute force:
try all combinations of a/b and <= target

for all a
    for all b
        compute


try different combinations


O(n*m)


test cases:

if same then you good

var
dict[target-b,id]

1. go through b and store complements

1. make b_dict complement O(b)
2. if a - b, target - a
3. for element in a find if there O(a)

# store largest as you go along

a = [0]
b = [9,8]

target = 10

1. find largest that is <= target, also store dict values
2. find all indexes at that value


1. sort a and b O(n log n)
2. left a/right b O(k-largest array)
'''


def findPairs(a,b,target):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    l, r = 0, len(b) - 1
    res = []
    largest = float('-inf')
    while (l<len(a) and r >= 0):
        id1, i = a[l]
        id2, j = b[r]
        psum = i + j
        if psum == largest:
            res.append([id1, id2])
        elif psum > largest and psum <= target:
            res = [[id1, id2]]
            largest = psum

        if psum < target:
            l += 1
        else:
            r -= 1
    return res

'''
[1,2,3,4]
l

[1,2,3,4]
        r

target = 3
'''



a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
print(findPairs(a,b,target))

# Lesson: 1. break down what you need to different processes.
# for example
# 1. process multiple if statement for res appends 2. update pointer multiple statements
# practice left and right pointers changing

