# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution
state

i - item considered
days left -
return - int min_all_containers_used

state transition

base case:
i<0 and days_left = 0: return 0
i<0 and days_left >=0: return inf
days_left ==0: return inf

recursive case: have days left and valid i
min_contain_size = inf
curr_max = -inf
for all items:
    #use it
    curr_max = max(curr_max,item[i])
    use = curr_max+min_allcontain(i-1,j-1)
    # don't use
    #no_use = min_allcontain(i-1,j-1)
    min(min_contain_size,use)

either use item or not

