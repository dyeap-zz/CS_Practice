'''
# longest word in D that is subseq of S

# 1. order matters
# 2. dictionary, window?

compare dictionary
dictionary is empty at end

dictionary = {
    a:1
    b:1
    l:1
    e:1
}

1. one ptr start with first letter once you find then move ptr up
2. if you reach end then replace with longest


var 
longest_word
D_ptr

for word in D

func D is subseq of S


longest_word = 
1. store as you go along
2. 

'''
'''
S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}


def is_subseq(S,word):
    ptr = 0
    for char in S:
        if (word[ptr] == char):
            ptr += 1
            if ptr == len(word):
                return True
    return False

def longest_word(S,D):
    longest = ""
    for word in D:
        if (is_subseq(S,word) and len(word) > len(longest)):
            longest = word
    return longest

print(longest_word(S,D))


'''
'''
#Given a non-empty string like "Code" return a string like "CCoCodCode".

#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'

1. print first letter. start over print the next one

var
sub_res
res
res += sub_res
1. concatenate string

# n is number of character in string
# concatenation is O(n)
# take a hit on performance O(n)
#O(n^2)

for char in string:
    sub_res.append(char)
    res += sub_res
return res

1. calculate len of res needed
2.

len_str = len(string)
for i in range(1,len(string)):

len_str = [None] * len_str
'''

'''
#Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)


#maxSpan([1, 2, 1, 1, 3]) → 4
#maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
#maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6

1. store the min and max index
2. subtract and calculate max span
'''


def max_span(nums):
    d = {}
    for i,num in enumerate(nums):
        if num not in d:
            d[num] = [i,i]
        else:
            val = d[num]
            d[num] = [val[0], i]
    res = 0
    for val in d.values():
        span = val[1] - val[0] + 1
        res = max(res,span)
    return res

print(max_span([1, 4, 2, 1, 4, 4, 4]))
# n is number of int in n
# m is number of unique number in n
# worst case m are al different integers
# time = O(n+m) -> O(n+n) -> O(2n) -> O(n)
# space = O(n) for dictionary


#Given two strings, base and remove, return a version of the base string where all instances of the remove string have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".


#withoutString("Hello there", "llo") → "He there"
#withoutString("Hello there", "e") → "Hllo thr"
#withoutString("Hello there", "x") → "Hello there"

'''
1. remove the elements
2. keep track of elemnts skip length of string when you find one

vars

do appends to list for string size

if != then append first letter to res

test cases:

hell, ell
l, zz
'''
'''
def withoutString(string,sub_string):
    res = []
    i = 0
    size = len(sub_string)
    while (i < len(string)):
        if (string[i:i+size] == sub_string):
            i += size
        else:
            res.append(string[i])
            i += 1
    return "".join(res)

print(withoutString("he", "hee"))

'''
#Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)

#sumNumbers("abc123xyz") → 123
#sumNumbers("aa11b33") → 44
#sumNumbers("7 11") → 18

#1. if number add to digit
#2. else perform adding and reset

#var
#multiplier = 0,10,100

'''
curr_num = 9
def sum_numbers(string):
    res = 0
    curr_num = 0
    for char in string:
        if (char.isnumeric()):
            curr_num *= 10
            curr_num += int(char)
        else:
            res += curr_num
            curr_num = 0
    return res + curr_num

print(sum_numbers("012"))
'''

#Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.


#canBalance([1, 1, 1, 2, 1]) → true
#canBalance([2, 1, 1, 2, 1]) → false
#canBalance([10, 10]) → true
'''
1. split and check both sides
2.


# brute/ divide then have func to calculate the sum

# some how keep running sum of both sides
do one inital run through to store sums


must have 2
vars

L,R = 0

L = L+prev
R = R-prev+curr


def canBalance(nums):
    if (len(nums) < 2):
        return False
    for i in range(1,len(nums)):
        left = nums[0:i]
        right = nums[i:]
        if (sum(left) == sum(right)):
            return True
    return False
print(canBalance([10,10,0]))
'''


# Modify and return the given map as follows: if the key "a" has a value, set the key "b" to have that same value. In all cases remove the key "c", leaving the rest of the map unchanged.
#
#
# mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
# mapShare({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
# mapShare({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}
'''
1. if a exists -> set b to dict[a]
2. delete c key if there
3. other leave same

vars
dict



def mapShare(map):
    if "a" in map:
        map["b"] = map["a"]
    if "c" in map:
        del map["c"]
    return map
print(mapShare({"a": "aaa", "c": "meh", "d": "hi"}))

'''

'''
#
#Write a simple interpreter which understands "+", "-", and "*" operations. Apply the operations in order using command/arg pairs starting with the initial value of `value`. If you encounter an unknown command, return -1. interpret(1, ["+"], [1]) → 2 interpret(4, ["-"], [2]) → 2 interpret(1, ["+", "*"], [1, 3]) → 6


#interpret(1, ['+'], [1]) → 2
#interpret(4, ['-'], [2]) → 2
#interpret(1, ['+', '*'], [1, 3]) → 6

def interpret(start,operations, values):
    res = start
    for i,op in enumerate(operations):
        if (op == '+'):
            res += values[i]
        elif (op == '-'):
            res -= values[i]
        elif (op == '*'):
            res *= values[i]
        elif (op == '/'):
            res /= values[i]
        else:
            return -1
    return res

print(interpret(1, ['+', '*'], [1, 3]))

'''

#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return true if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

#makeBricks(3, 1, 8) → true
#makeBricks(3, 1, 9) → false
#makeBricks(3, 2, 10) → true

#can be done without for loops

#1. some combination of bricks to get goal
# coin change problem bottom up

'''
1. base case - no more bricks or goal is negative return False.
2. base case - goal == 0 return True
3. use coin and one without coin

limited number of coins

if multiple of 5
    1. use as many 5 brickes (divide)
if num of ones brick is larger than new goal

num_big = 1
num_big = 2
num_big = 3

goal = 10

base case
if have enough ones then True

use a 5 

if no more 5 return false

num_big = 1
num_big = 2
num_big = 3

goal = 10


big = 1 small = 5 goal = 10

if (goal>big*5+small):
1. ensure you have enough coins for goal
2. ensure you have enough ones coins for goal

all you can do it

instead of all true cases
return False

# how to guaratnee you have enough big coins
num_ones_coins_needed > num_small_coins

def make_bricks(num_small, num_big, goal):
    if (goal <= num_small):
        return True
    if (num_big < 1 or goal < 1):
        return False
    return make_bricks(num_small,num_big-1,goal-5)
print(make_bricks(1000000, 1000, 1000100))
'''

def make_bricks(small,big,goal):
    # what makes this code not work
    # check you have enough coins big and small coins
    if (goal > big * 5 + small): return False;
    # check you have enough ones coins
    if (goal % 5 > small): return False;
    return True;

