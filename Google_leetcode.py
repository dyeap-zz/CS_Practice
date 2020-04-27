# https://leetcode.com/discuss/interview-question/352458/

def min_char_count(string):
    my_dict = {}
    for char in string:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    min_char_occ = list(my_dict.items())[0]
    for tup_char_occ in my_dict.items():
        if (min_char_occ[0] > tup_char_occ[0]):
            min_char_occ = tup_char_occ
    return min_char_occ

def min_strings(A, B):
    res = []
    li_A = A.split(',')
    li_B = B.split(',')
    for string_B in li_B:
        tot_min_occ = 0
        for string_A in li_A:
            low_B = min_char_count(string_B)
            low_A = min_char_count(string_A)
            if (low_B[0] < low_A[0] or (low_A[0] == low_B[0] and low_A[1] < low_B[1])):
                tot_min_occ += 1
        res.append(tot_min_occ)
    return res

A = "ad,bc,bd"
B = "zdnv,kdfj"
print(min_strings(A,B))


for i in range(3):
    print(i)

p = []
z = []
z.append(1)
print(z)


class Solution(object):
    def is_pal(self, word):
        if len(word) == 1:return True
        size_word = len(word)
        for i in range(size_word // 2):
            if (word[i] != word[size_word - i - 1]):
                return False
        return True

    def help_partition(self, s, path, res):
        # base case
        if (len(s) < 1):
            res.append(path)

        for i in range (1,len(s)+1):
            # add letter to last path
            temp = s[:i]
            if (self.is_pal(temp)):
                self.help_partition(s[i:], path+[temp], res)


    def partition(self, s):
        res = []
        path = []
        self.help_partition(s, path, res)
        return res
sol = Solution()

print(sol.partition("aab"))


print(list("aa"))


l = [[]]*10
print(l)

print(isinstance(1,int))
