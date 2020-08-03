'''
longest increasing subsequence

EX: [1,2,0,2,7]

return the long increasing subsequence

EX: [] -> 0
[1] -> 1
[0,-1] -> 1
[1,2] -> 2
[3,1,2] -> 2
negatives numbers are allowed

1. states
index being considered - i
prev_num being - prev_num
return max increasing subseq

ex

[1,2,0]

2. transitions
start with i = 0
solve(nums,i)
# base case
if reach end of list: 0
# recursive case
res = solve(i+1)
res = 0
for all numbers
    res = max(res,solve()

return res

recurrence relation
sol(i) =  max(sol(i+1),)

every step we either choose to use the number of we don't
i = 0
either use the number or dont
use =
don't use = solve(i+1)
if curr_num > next_num
max(solve(),)

solve(i+1)
How do we use less variables and
[1,2,-100,3]
The idea is you have different starting index
for that particular problem you solve for that then move the starting index


1. states
prev_num or index of last number considiered - i
return max_number

2. state transitions
start with i = -1
solve(prev_num,profit)
# base case
    if i is last num: return 1
# recursive case
    res = 0
    not use = solve(i)
    for idx in all nums
    use = solve(idx)
    max(use,not_use)
return max

recurrence relation
not_use = sol(i+1)
use = 1+sol(i+1)
sol(i)=max(sol(i+1),1+sol(i+1)) for i = 0,1,2,...len(nums)

to use it the curr number must be less than prev num
if curr num > prev num:
    1+sol(idx+1)
else:
    sol(idx+1)


'''

def lis(nums, i,dp):
    # base case
    if i == len(nums)-1: return 1
    # recursive case where i is not last item
    if dp[i] != -1: return dp[i]
    res = 0
    for idx in range(i+1,len(nums)):
        # allowed to use num
        if nums[idx] > nums[i]:
            ans = 1+lis(nums,idx,dp)
        # not allowed to use num
        else:
            ans = lis(nums,idx,dp)
        res = max(res,ans)
    dp[i] = res
    return dp[i]

nums =  [1,2,0,9,4,1,3,10,8]
dp = [-1] * len(nums)
print(lis(nums,0,dp))

'''
#bottom up approach
change the dp equation

1. create a dp array what size? +1
dp = nums + 1
2. base case
the 0 index of dp is empty list
dp[0] = 0
3. alg
use = 1+dp[i-1] # if you used the number
not_use = dp[i-1] # if you didnt use the number
dp[i] =
for i - end index:
    res = 0
    if last index res = 1
    for j - item being considered:
        # allowed to use num
        if nums[j] > nums[i]:
            ans = 1+dp[j]
        # not allowed to use num
        else:
            ans = dp[j]
        res = (res,ans)
    dp[i] = res

'''
# good solution
def lis_bot_up(nums):
    # create dp array
    dp = [0] * len(nums)

    # base case
    dp[0] = 1

    # alg
    for i in range(1,len(dp)):
        #res = 0
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i],1+dp[j])
            #else:
            #    ans = dp[j]
            #res = max(res,ans)
        #dp[i] = res
    print(dp)
    return max(dp)

#nums = [1,2,0,7]
#dp = [1,2,0,3]
print(lis_bot_up(nums))

def lis_bot_up(nums):
    # create dp array
    dp = [0] * len(nums)
    prev_index = [-1] * len(nums)
    # base case
    dp[0] = 1

    # alg
    for i in range(1,len(dp)):
        for j in range(i):
            if nums[j] < nums[i]:
                if 1+dp[j] > dp[i]:
                    prev_index[i] = j
                dp[i] = max(dp[i],1+dp[j])

    # reconstruct
    max_index = prev_index[0]
    for i in range(len(prev_index)):
        if max_index<dp[i]:
            max_index = i

    res = []
    i = max_index
    print(i,type(i))
    print(prev_index)
    while(i>=0):
        res.append(i)
        if prev_index[i] == -1: break
        i = prev_index[i]
    print(res)

    return max(dp)

print(lis_bot_up(nums))
z = "".join(["a","a"])
l = "bcc" *  2
print(z)