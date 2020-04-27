import heapq

# implement max heap using min_heap
# https://sisyphus.gitbook.io/project/python-notes/python-priority-queue-heapq
# muliply all values by -1 and when you pop mulitply back to get original value

s = [(1,3)]
print(type(s[-1][1]))

if (s):
    print("s")

nums = [1,10,4,6,8,2,8,9,1,10]

heapq.heapify(nums)
heapq.heappush(nums,5)
heapq.heappop(nums)
print(nums)


heap = [3,2,1,4]


num = [2,0,2,1,1,0]

for i,number in enumerate(num):
    num[i] = -1*number


heapq.heapify(num)

for i in range(len(num)):
    temp = num[len(num)-1-i]
    num.append(heapq.heappop(num) * -1)
    heapq.heappush(num,temp)
    #heapq.heapify(num[i:len(num)-1-i])
    print(num)

print(num)

print()

