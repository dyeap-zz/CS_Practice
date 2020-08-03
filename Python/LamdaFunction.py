# https://www.youtube.com/watch?v=25ovCm9jKfA
# lambda functions are good if you only need to use the function once such as in for loop
# lamda (input/parameter of your anonymous function): (return of anonymous function)

# map takes a function and your input. Applies input to your function
# map(func,iterable) - takes all elements in iterable and runs it through the function

# always returns 4
lambda: 4

y = lambda item: item*2
z = 3
print(y(z))

x = [1,2,3]
def mult2(num):
    return num*2

print(list(map(mult2,x)))
print(list(map(lambda num: num*2, x)))




print(map(lambda item: item*2,x))

print(lambda:5)
from collections import defaultdict
marks=defaultdict(lambda:35)
marks[1]
print(marks.items())

for key,val in marks.items():
    print(key,val)


import random
randomlist = []
for i in range(0,5):
    n = random.randint(1,30)
    randomlist.append(n)
print(randomlist)

import itertools

nums = [1,2,"3"]


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    return (a,b)
    #next(b, None)
    #return list(zip(a, b))
print(pairwise(nums))