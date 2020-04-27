def sort_stack(s1):
    s2 = []
    while(s1):
        if (len(s2) == 0):
            s2.append(s1.pop())
        elif (s1[-1] > s2[-1]):
            s2.append(s1.pop())
        else:
            s2[-1],s1[-1] = s1[-1],s2[-1]
            s1.append(s2.pop())
    return s2

nums = [-1,4,0,3,1,2]
print(sort_stack(nums))

adict = {}
adict[(2,1)] = 2
print(adict[(2,1)])

num1 = 14
num2 = 31


print(num1^num2)
c = num1^num2
count = 0
c = 7
while(c != 0):
    count += 1
    print(format(c,"b"))
    print(format(c-1,"b"))
    print(format(c&(c-1),"b"))
    c = c& (c-1)
print(count)

res = []
res.append([])
res[0].append(2)
print(res)

res = [1,2,3]
print(res[-2:4])



















def removeDuplicates(s, k):
    stack = [[s[0], 1]]
    for c in s[1:]:
        if stack and c == stack[-1][0]:
            stack[-1][1] += 1
        else:
            stack.append([c, 1])
        if stack[-1][1] == k:
            del stack[-1]
        # print(stack)
    return ''.join([i[0] * i[1] for i in stack])


removeDuplicates("deeedbbcccbdaa",3)


li1 = [1,2,3]
li1 = [1,2,4,5]

# for [0,len(li1)]:
#   for L in [1,len(li)]
#       R = L + 1
#       if (li[L]>li[R])
#           swap()

# need a L/M/R ptr
# if target is greater > L and less than M.
#   we know on left side
# if target is less than R and greater than M we know it's on the right side
#   we know on R side
target = 2
#Binary Search

def BinarySearch(nums,target):
    if (len(nums) < 1):
        return -1
    left = 0
    middle = math.floor(len(nums)/ 2)
    if (nums[middle] == target):
        return middle
    elif(target < nums[middle]):# left side
        return BinarySearch(nums[left:middle], target)
    else: # right side
        return BinarySearch(nums[middle + 1:], target)
    return -1


# [2] -> 0
# [1,2] -> 1 middle = 0
# [2,3] -> 0
# [1,2,3] -> 1
# [1,2,3,4] -> 1 middle = 2
# [0,1,2,3] -> 2
target = 2
1,2
0,1

#L/M/R = 0/0/1
print(BinarySearch(li1,target))



#Bubble Sort
for start in range(0,len(li1)):
    for left in range(start,len(li1)-1):
        right = left + 1
        if (li1[left] > li1[right]):
            li1[left], li1[right] = li1[right],li1[left]
print(li1)






def mult2(val):
    return str(val)
print(list(map(mult2,li1)))


di_1 = {
    "1":4,
    "2":5
}

di_2 = {
    "6":6,
    "7":7,
    "8":8
}



for kv1,kv2 in zip(di_1.items(),di_2.items()):
    print(kv1.count(4))
    print(kv1, kv2)

def say_hello():
    print("hi")
print(not 0)
