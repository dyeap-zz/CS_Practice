from collections import defaultdict
'''
class Solution:
    def dfs(self, city, out, inc, res):
        # base case
        if len(out) == 0 and len(inc) == 0: return True
        if city not in out: return False

        # recursive case - more edges left
        neighbors = list(out[city])
        neighbors.sort()
        for nei in neighbors:
            # erase edge and go to the nei
            res.append(nei)
            out[city].remove(nei)
            if len(out[city]) == 0: del out[city]
            inc[nei].remove(city)
            if len(inc[nei]) == 0: del inc[nei]
            if self.dfs(nei, out, inc, res):
                return True
            # not a valid path - update
            res.pop()
            out[city].add(nei)
            inc[nei].add(city)
        return False

    def findItinerary(self, tickets):
        out = defaultdict(set)
        inc = defaultdict(set)
        for a, b in tickets:
            out[a].add(b)
            inc[b].add(a)
        res = ["JFK"]
        self.dfs("JFK", out, inc, res)
        return res

'''
class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]





#tix = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
tix = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
sol = Solution()
print(sol.findItinerary(tix))



#a = list(set(["fd","asd"]))
#a.sort()

#print(a)