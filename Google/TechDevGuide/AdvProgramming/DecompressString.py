'''
The input

3[abc]4[ab]c

Would be output as

abcabcabcababababc



'''
'''
1. reach end of string letters left

var
list? fast appends one letter at time
ptr R->left
stack(word,num)
res
counter

default num of string
if let with no num



stack
1. process number
2. process word


ptr R->left
stack(word,num)
res
counter

1. push everything onto stack (letter,num)
2. pop everything off stack and process

def process_word(string,i):
    right = i
    left = i
    while(string[left].isalpha()):
        left -= 1
    return left,string[left+1:right + 1]

def process_num(string,i):
    num = 0
    pow = 0
    while(string[i].isnumeric()):
        left_num = int(string[i]) * 10**pow
        num += left_num
        pow += 1
        i -= 1
    return i, num

def decompress_string(string):
    res = ""
    stack = []
    i = len(string) - 1
    while (i >=0):
        if string[i] == ']':
            i -= 1
            i, word = process_word(string,i)
            i -= 1
            i, num = process_num(string,i)
            stack.append((num,word))
        else:
            i, word = process_word(string, i)
            stack.append((1,word))

    while (stack):
        numWord = stack.pop()
        res += numWord[1] * numWord[0]

    return res



print(decompress_string("2[3[a]b]"))

# redo

    if left == char:
        process until not letter + decompress()

    elif number
        1. process number until not number
        2. decompress rest
        3. res = num*deompress
    else:
        instruction None
'''
'''
def decompress_string(string):
    if (string == ""):
        return ""

    first_char = string[0]
    i = 0

    if first_char == ']' or first_char == '[':
        return decompress_string(string[1:])

    elif (first_char.isalpha()):
        while(string[i].isalpha()):
            i += 1
            if (i == len(string)):
                break
        return string[0:i] + decompress_string(string[i:]) # v2

    else: # must be a number
        while(string[i].isnumeric()):
            i += 1
        num = int(string[:i])
        return num * decompress_string(string[i:])

print(decompress_string("a3[ty]u3[ar]"))


abc
13[a]
13[a]b
v15[c]
2[3[a]b]

recursion
'''




