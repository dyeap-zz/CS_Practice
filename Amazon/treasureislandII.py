#https://leetcode.com/discuss/interview-question/356150
'''
Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
'''

#1. BFS except starting queue will have three points
# for testing try breaking it

# unknown
# 1. understand the problem
# 2. work through an example
# 3. build a solution - brute force solution
# 4. test brute force with normal inputs, corner cases, how would you do it and what data structures would you use, analyze time and space complexity
# 5. once you have thorough analysis then write code