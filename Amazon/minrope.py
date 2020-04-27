# https://leetcode.com/discuss/interview-question/344677

# pattern to connecting ropes in different ways

# brute force back track and try all combination
'''
[1,2,4,5]

connect smaller first

cost = 3 + 9 + 12 = 24
cost = 6 + 11 + 12 = 29
cost = 6 + 7 + 12 = 25

min_cost is to connect those close in length


[8, 4, 6, 12]

10 + 18 + 30

20, 4, 8, 2

2,4,8,20

cost = 6+14+34 = 54

1,99,100

100 + 200

199 + 200 =



2,2,3,3

4 + 6 + 10 = 20
6 + 4 + 10 = 20

1,4,100

(100 + 4) + ((100+4)+1)

(1+4) + ((1+4) + 100) = 110


2,2 100,102

4 + 104 + 104+102

1. want to connect min together



1, 2, 5, 10, 35, 89

3 + 8 + 18 + 18+35 + 18+35+89


1. sort array preform addition
2. need some way to put it back into list
'''
'''
1. compute 2 smallest number
2. put that number back into sorted list
3. go until one rope

realization is that you do not want large rope values to compound during additon

python only max heap


heapify O(n)
heapop O(logn) to restore
heapinser O(logn) to restore

heapify
while (more than one rope)
    choose two smallest add
    heapinsert O(log n)
'''
import heapq
def minCost(ropes):
    #ropes = list(map(lambda x: -1*x,ropes))
    if len(ropes) == 0: return 0
    if len(ropes) == 1: return ropes[0]
    heapq.heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        rope1, rope2 = heapq.heappop(ropes), heapq.heappop(ropes)
        newRope = rope1 + rope2
        cost += newRope
        heapq.heappush(ropes,newRope)

    return cost

ropes = [5]
print(minCost(ropes))