# Duck Type

class Airplane:
    def fly(self):
        print("Airplane flying")
class Bird:
    def fly(self):
        print("Bird flying")
for obj in Airplane(),Bird():
    obj.fly()

# Operator Overloading
class Student:
    def __init__(self,score):
        self.score = score
    def __add__(self,other):
        s3 = Student(self.score + other.score)
        return s3

s1 = Student(90)
s2 = Student(100)
s3 = s1+s2
print(s3.score)
# Method overloading

def sum(val1,val2=0):
    return val1+val2

print(sum(1))

# Operator Overriding
class A:
    def explore(self):
        print("explore() method from class A")


class B(A):
    def explore(self):
        print("explore() method from class B")


b_obj = B()
a_obj = A()

b_obj.explore()
a_obj.explore()


# bit manipulation

print(1 << 2)
print(~0)

sum = 0
for i in range(3):
    sum = sum ^ i
print(sum)


def Add(x, y):
    # Iterate till there is no carry
    while (y != 0):
        # carry now contains common
        # set bits of x and y
        carry = x & y

        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y

        # Carry is shifted by one so that
        # adding it to x gives the required sum
        y = carry << 1

    return x
print(Add(3,5))



class Solution(object):
    #memo = {} # amount: min num coins
    def __init__(self):
        self.memo = {}
    def coinChange(self,coins, amount):
        if (amount < 0 or (len(coins) == 0 and amount > 0)):
            return 0
        if (amount == 0):
            return 1
        #if amount in self.memo:
        #    return self.memo[amount]
        #self.memo[amount] = self.coinChange(coins[1:],amount) + self.coinChange(coins[:],amount-coins[0])
        return self.coinChange(coins[1:],amount) + self.coinChange(coins[:],amount-coins[0])

solu = Solution()
coins = [1,2]
print(solu.coinChange(coins,3))





class Solution:
    memo = {}
    def coinChange(self, coins, amount):
        if (amount < 0):
            return -1
        if (amount == 0):
            return 0
        if amount in self.memo:
            return self.memo[amount]
        min_coins = float('inf')
        self.memo[amount] = -1
        for coin in coins:
            remainder = amount - coin
            sub_min_coins = self.coinChange(coins,remainder)
            #print(sub_min_coins,amount)
            if (sub_min_coins >= 0 and sub_min_coins < min_coins):
                min_coins = min(1+sub_min_coins,min_coins)
            print(min_coins)
            if (sub_min_coins > 0):
                self.memo[amount] = min_coins
        print(self.memo,amount)
        return self.memo[amount]
sol = Solution()
print(sol.coinChange([1,2,5],11))


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        for i in range(1, int(n**0.5)+1):
            dp[i**2] = 1

        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-k**2]+1)

        return dp[n]

sol = Solution()
sol.numSquares(16)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))

print("s")
s = "asdf]"
print(s[4].isalpha())

def ret():
    return 1,None

x,y = ret()
print(x,y)


print(int(4**(1/2)))


if 1 < 2 < 3: print(True)

for (m,n) in [(-1,0),(1,0),(0,1),(0,-1)]:
    print(m,n)
import sys
nums = [1,2,3]
res = [] * len(res)
print(res,sys.getsizeof(res))

