# 5*4!
# 4!

def factorial_iter(num):
    ans = 1
    while(num):
        ans *= num
        num -= 1
    return ans


def factorial(num):
    if (num == 0):
        return 1
    return num * factorial(num-1)

print(factorial(8))
print(factorial_iter(8))

#5
#3
#0 1 1 2 3
def fib_iter(index):
    if (index == 0):
        return 0
    if (index == 1):
        return 1
    res = 0
    prev_num = 0
    num = 1
    for _ in range(0,index-1):
        res = num + prev_num
        prev_num = num
        num = res
    return res
print(fib_iter(8))

#5
#3
#0 1 1 2 3


def fib(index):
    if (index < 1):
        return 0
    if (index == 1):
        return 1
    return fib(index-2) + fib(index-1)

print(fib(8))