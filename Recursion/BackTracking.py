'''
Backtracking format
Function (input,partial,output)
If partial solution is valid solution{
	Process solution
}
Candidate = generateCandidate()
For c in candidate{
1.	Add candidate to partial
2.	Recuse function with partial
3.	Remove candidate
}
'''


def perm(nums,used,path,res):
    if len(path) == len(nums):
        #print(len(path))
        res.append(path)
        return
    for i,num in enumerate(nums):
        if used[i] == 1: continue
        # num has not bee used
        used[i] = 1
        path.append(num)
        perm(nums,used,path[:],res)
        # undo the move
        used[i] = 0
        path.pop()

nums = [1,2,3]
used = [0] * len(nums)
res = []
perm(nums,used,[],res)
print(res)

'''
Given an input array and an integer 'K' which is atmost size of the array,
generate all the ways we can choose K integers from the array
EX: [3,2,5,8] k=3
[3,2,5]
[3,2,8]
[3,5,8]
[2,5,8]

backtracking:
solve(nums, i,k, path)
# base case
if len path == k: store it
if i<k: 
# recursive case at n>=k
# go through all nums by trying to add them to path
for all nums
    # add to path
    solve(i+1) # prevent using numbers already used
    # remove from path

'''
res = [[3,2,5],[3,2,8],[3,5,8]]
path = [3,5,8]
i = 0
def comb(nums, i, k, path, res):
    # base case
    if len(path) == k:
        res.append(path[:])
        return
    #if i == len(nums): return
    # recrusive case
    for idx in range(i,len(nums)):
        path.append(nums[idx])
        comb(nums,idx+1,k,path,res)
        path.pop()

nums = [3,2,5,8]
k = 3
res = []
comb(nums,0,k,[],res)
print(res)

#3 [2,5,8]
#3,2 [5,8]
#3,2,5 [8]

'''
Another way to do combination but this algorithm can be used to find optimal solution to all subset
in set
idea:
either include it in set or don't

solve(num,i,k,path)
# base case
if len of path == k: add to res
if i is <= len(nums):ret
# recursive case
solve(add num to path)
solve(don't add)
both must i+1
'''

def comb2(nums,i,k,path,res):
    # base case
    if len(path) == k:
        res.append(path[:])
        return
    if i == len(nums): return
    # recursive case
    path.append(nums[i])
    comb2(nums,i+1,k,path,res)
    path.pop()
    comb2(nums,i+1,k,path,res)

res = []
comb2(nums,0,k,[],res)
print(res)

'''
N Queen
get list of all (r,c) of queens

1. path - list (r,c)
2. func check if queen can be placed there

recursion if can put in col move to next row
# base case
if last row + 1- add to res
# recrusive case
for all col
    try placeing queen
    if can place queen:
        recurse to next row
    remove queen from path
    
[]
func validqueen
if no queen in list: add to path
visited row,col
diag visited that holds set of r,c
for all queens
    1. check horz,vert,diag
        horz - same row
        vert - same col
        diag - same diag
    2. update row,col,diag visited
'''

def valid_path(n,path):
    v_row, v_col, v_diag = set(),set(),set()
    for r,c in path:
        if r in v_row: return False
        if c in v_col: return False
        if (r,c) in v_diag: return False
        # update visited sets
        v_row.add(r)
        v_col.add(c)
        temp_r,temp_c = r,c
        # add backwards
        while temp_r < 0 or temp_c < 0:
            v_diag.add((temp_r,temp_c))
            temp_r -= 1
            temp_c -= 1
        # add forwards
        temp_r, temp_c = r+1, c+1
        while temp_r < n or temp_c < n:
            v_diag.add((temp_r,temp_c))
            temp_r += 1
            temp_c += 1

    return True

def n_queen(n,row,path,res):
    # base case
    if row+1 == n:
        res.append(path[:])
    # recursive case
    for col in range(n):
        path.append((row,col))
        if valid_path(n,path):
            n_queen(n,row+1,path,res)
        path.pop()


res = []
n=2
for i in range(n):
    n_queen(n,i,[],res)
print(res)

'''
Given a list of numbers, and a target number. Print all unique combinations
in candidates where the candidate numbers sum to target. 

EX: 
in: [10,1,2,7,6,1,1,5], target = 8

output:
[1,1,6]
[1,2,5]
[1,7]
[2,6]

[1,2,5]
# outline

1. keep adding numbers until you go over target
2. if you add it and it goes over target try adding another number

this will prevent same answers
iterate through multiple points
# helper 

gen_perm
solve(nums,i,prev,target,path,res)
# base case
if last index+1: ret
if target is 0: add to res
# recursive
for all nums -idx
    add nums to path
    if valid_path
        recrusve(target-num,prev)
    remove num
    
how to check for unique sets?
use a dictionary and sort the answers
or use a dictionary key is {value:different sets that add up to value}

1. sort the array if the res 

[1,1,1,2,5,6,7,10] target = 8
1. to prevent duplicates. 
can only choose numbers that are different than prev selected number
'''

nums = [10,1,2,7,6,1,1,1,5]
target = 8

def unique_comb(nums,i,target,path,res):
    # base case
    if i == len(nums): return
    if target == 0:
        res.append(path[:])
        return
    #prev = float('-inf')
    # recursive
    for idx in range(i,len(nums)):
        num = nums[idx]
        # check duplicate
        if idx > i and (nums[idx] == nums[idx-1]): continue
        # make move
        path.append(num)
        target -= num
        # check if valid move
        if target >= 0:
            unique_comb(nums, idx+1, target, path, res)
        # undo move
        path.pop()
        target += num
        #prev = num


res = []
nums.sort()
unique_comb(nums,i,target,[],res)
print(res)