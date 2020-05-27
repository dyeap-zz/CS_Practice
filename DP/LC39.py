

def combinationSum(candidates, target, index, path, res):
    # base case
    if target == 0:
        res.append(path[:])
        return
    if target<0 or index == len(candidates): return
    # recursive - target is pos and we need to use a candidate
    for i in range(index,len(candidates)):
        num = candidates[i]
        path.append(num)
        # make the move
        combinationSum(candidates,target-num,i,path, res)
        path.pop()


res = []
combinationSum([1,2],5,0,[],res)

print(res)
'''
# base case
1. target = 0: return candidate[index]
2. if target<0 or index over: return []
# 
how to keep track of numbers used?

return comb(use candidate) + comb(don't used candidate)
'''
def dfs(candidates, target, index):
    # base case
    if target == 0: return candidates[index]
    if target < 0 or index == len(candidates): return
    # recursive case
    
