'''
Input: A = [1,15,7,9,2,5,10], K = 3

A = [1,15,7,9,2,5,10]

must generate all possible partition of subarray

for all starting points i: 0-n
	for all window size: 1-K
		find max in the window.
			res = max(res,get_max_sum(i+1,K))

'''
def max_win_sum(nums,i,K,dp):
    # base case
    if i >= len(nums): return 0
    # recurisve case
    if dp[i] != -1: return dp[i]
    res = float('-inf')
    for idx in range(i,len(nums)): # 0
        #max_win = min(len(nums)-idx, idx+K)
        for w in range(1,K+1): # 1,2,3
            #if w == 1: max_num = nums[idx]
            max_num = max(nums[idx:idx+w])
            if idx + w >= len(nums)+1: mult_w = len(nums) - idx
            else: mult_w = w
            res = max(res,max_num*mult_w + max_win_sum(nums,idx+w,K,dp))
    dp[i] = res
    return res


def max_win_sum(nums,i,K,dp):
    # base case
    if i >= len(nums): return 0
    # recurisve case
    if dp[i] != -1: return dp[i]
    res = float('-inf')
    for idx in range(i,len(nums)): # 0
        #max_win = min(len(nums)-idx, idx+K)
        for w in range(1,K+1): # 1,2,3
            if idx + w > len(nums): break
            #if w == 1: max_num = nums[idx]
            max_num = max(nums[idx:idx+w])
            #if idx + w >= len(nums)+1: mult_w = len(nums) - idx
            #else: mult_w = w
            res = max(res,max_num*w + max_win_sum(nums,idx+w,K,dp))
    dp[i] = res
    return res

#15 * 3 + 9
A = [1,1,1,2,3,10,8]
K = 3
dp = [-1] * (len(A))
print(max_win_sum(A,0,K,dp))
print(dp)

#solve(nums,0,K)

#1+solve(nums,1,K)

#solve(i) = max_num of (nums[i:i+K]) * windows size + solve(i+1)

'''
bottom up:
1. size of dp array? same as len(nums) start as all 0
2. extra algotihm to store base case? nope
3. actualy iteration
'''
'''
for idx in range(i, len(nums)):  # 0
    # max_win = min(len(nums)-idx, idx+K)
    for w in range(1, K + 1):  # 1,2,3
        # if w == 1: max_num = nums[idx]
        max_num = max(nums[idx:idx + w])
        if idx + w >= len(nums) + 1:
            mult_w = len(nums) - idx
        else:
            mult_w = w
        res = max(res, max_num * mult_w + max_win_sum(nums, idx + w, K, dp))
        
  
1
2
3 
'''
def max_win_sum(nums,K):
    dp = [-1] * (len(nums)+1)
    dp[-1] = 0

    # Alg
    #res = float('inf')
    for idx in range(len(dp)-1,-1,-1):
        for w in range(1, K + 1):  # 1,2,3
            if idx + w > len(nums): break
            # if w == 1: max_num = nums[idx]
            # cover cases where window is too large
            max_num = max(nums[idx:idx + w])
            #if idx + w >= len(nums) + 1:
            #    mult_w = len(nums) - idx
            #else:
            #    mult_w = w

            # covers base cases where window is too large
            #if idx + w >= len(nums): prev_ans = 0
            #else: prev_ans = dp[idx+w]
            dp[idx] = max(dp[idx],max_num*w + dp[idx+w])
    print(dp)
    return dp[0]
print(max_win_sum(A,K))

A = [1,1,1,2,3,10,8]

[1,2,3,10,8]