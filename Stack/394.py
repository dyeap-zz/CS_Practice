def decodeString(s):
    stack = []  # 3,[,
    for char in s:
        if not (char == "]"):
            stack.append(char)
            continue
        # char is a closing para pop off stack until empty
        word = ""  # acc
        while stack[-1] != "[":
            word = stack.pop() + word
        # remove open
        stack.pop()
        word = word * int(stack[-1])
        # remove number
        stack.pop()
        while stack and stack != "[":
            word = stack.pop() + word
        # either have open para or empty stack
        stack.append(word)
    # extra characters leftover
    if len(stack) != 1:
        return "".join(stack)
    return stack.pop()




def decodeString(s):
    stack = [];
    curNum = 0;
    curString = ''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num * curString
        elif c.isdigit():
            curNum = curNum * 10 + int(c)
        else:
            curString += c
    return curString

s = "3[a2[c]]"
print(decodeString(s))

