
'''
1. stack
2. loop: string
3. if open brack: append to stack
4. if close and stack[-1] match don't match: return False
5. # match
6. pop(),

True if stack is empt else False
'''
from collections import deque
def balanced_bracket(s):
    stack = deque() # {,[

    for b in s:
        # open bracket
        if (b == '(' or b == '[' or b == '{'):
            stack.append(b)
            continue
        # closing bracket
        if (len(stack)==0 or not((stack[-1] == '(' and b == ')') or
                                 (stack[-1] == '[' and b == ']') or
                                 (stack[-1] =='{' and b == '}'))):
            return False
        stack.pop()

    return True if len(stack) == 0 else False

bracket = '{[}]'
print(balanced_bracket(bracket))
