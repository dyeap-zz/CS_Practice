def rob_helper(nums):
    if len(nums) == 0: return 0
    # at least one house to rob
    prev_rob = nums[0]
    prev_no_rob = 0
    rob, no_rob = prev_rob, 0
    res = max(prev_rob, prev_no_rob)
    for i in range(1, len(nums)):

        rob = max(rob, nums[i] + prev_no_rob)
        no_rob = max(no_rob, prev_rob)
        print(rob, no_rob)
        # update max
        res = max(rob, no_rob)
    return res

print(rob_helper([2,1,1]))

# https://leetcode.com/problems/house-robber-ii/discuss/59934/Simple-AC-solution-in-Java-in-O(n)-with-explanation