# top down approach dividing out left side
def rev_s(s):
    if (s == ""): return s
    return rev_s(s[1:]) + s[0]

print(rev_s("abc"))


dict = {}
dict[(1, 0)] = 1
if (2, 2) in dict:
    print("yes")
print(dict)

'''
def all_ways(nums,li_s):
    if (len(nums) == 0): return [[]]
    if (len(nums) < 2): return [[nums[0]]]
    li_s = all_ways(nums[1:],li_s)
    all_li = []
    for li in li_s:
        new_li = li[:]
        new_li.append(nums[0])
        all_li.append(new_li)
    li_s.append([nums[0]])
    li_s = li_s + all_li
    return li_s
'''
'''
s = "abc"
print(s[0])

def all_P(s,i,res):
    if (len(s) == 0): return res
    if (len(s) == i): return [s[i-1]]
    Pno_f = all_P(s,i+1,res)
    res = res + Pno_f
    for word in Pno_f:
        for j in range(0,len(word)):
            print(word[0:j],s[0],word[j:])
            new_word = word[0:j] + s[i-1] + word[j:]
            res.append(new_word)
        res.append(word+s[i-1])
    res.append(s[i-1])
    return res

print(all_P("abc",1,[]))
'''


def reverse_str(s):
    li = [None] * len(s)
    for i, let in enumerate(s):
        li[len(li) - i - 1] = let
    return "".join(li)


print(reverse_str("absdef"))


def all_P(s, i, res):
    if (len(s) == i):
        res.append(s)
        return res
    first_char = s[i]
    new_res = []
    for word in res:
        for j in range(0, len(word)):
            # print(word)
            # print(type(str(word[0:j])))
            new_word = word[0:j] + first_char + word[j:]
            new_res.append(new_word)
        new_res.append(word + first_char)
    return all_P(s, i + 1, new_res)


print(all_P("abc", 1, ['a']))


def all_comb(s, res):
    if (s == ""): return [s]
    for i in range(1, len(s) + 1):
        res.append(s[0:i])
    set_of_comb = all_comb(s[1:], res)
    res = res + set_of_comb
    return res


print(all_comb("abc", []))

'''
def all_comb(s,li_comb):
    if (len(s) == 0): return li_comb
    if (len(s) == 1):
        li_comb.append([s])
        return li_comb

    small_sub = all_comb(s[1:],list)
    for word in enumerate(small_sub):
        for i in range(len(word)):
            new_word = word[0:i] + str[0] + word[i:]
            li_comb.append([new_word])
    return li_comb

print(all_comb("abc",[]))
'''

# bottom up approach
'''
def rev_stack(stack,res):
    if (len(stack) == 0): return res
    val = stack.pop()
    res.append(val)
    return rev_stack(stack,res)
'''


# top down approach
def rev_stack(stack):
    if (len(stack) == 0): return []
    res = rev_stack(stack[1:])
    res.append(stack[0])
    return res


print(rev_stack([1, 2, 3, 4]))
'''
# bottom up approach
def atio(s,res):
    if (s==""): return res
    res = res * 10 + int(s[0])
    return atio(s[1:],res)

# top down
# breaking down the left side
def atio(s):
    global ten
    if (s==""): return 0
    left = atio(s[0:len(s)-1])
    res = left * 10 + int(s[-1])
    return res
'''
# top down
# breaking down and doing the right side
ten = 0


def atio(s):
    global ten
    if (s == ""): return 0
    right = atio(s[1:])
    res = right + 10 ** ten * int(s[0])
    ten += 1
    return res


print(atio("1234"))

li = [1]
print(li[-1:2])


def x(num):
    num = 3


num = [1]
x(num)
print(num)


def bb(nums,e):
    if (e<=1):return
    for i in range(0, len(nums) - 1):
        if (nums[i] > nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    bb(nums,e-1)
    return

''''
def bb(nums):
    if (len(nums) == 1): return [nums[0]]
    for i in range(0,len(nums)-1):
        if (nums[i]>nums[i+1]):
            nums[i],nums[i+1] = nums[i+1],nums[i]
    sort_left = bb(nums[0:len(nums)-1])
    sort_left.append(nums[-1])
    return sort_left
'''
nums = []

print(bb(nums,len(nums)))
print(nums)



