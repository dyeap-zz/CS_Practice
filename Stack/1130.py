def mctFromLeafValues(A):
    res = 0
    stack = [float('inf')]
    for a in A:
        while stack[-1] <= a:
            mid = stack.pop()
            res += mid * min(stack[-1], a)
        stack.append(a)
    while len(stack) > 2:
        res += stack.pop() * stack[-1]
    return res

A = [1,2,3]
print(mctFromLeafValues(A))