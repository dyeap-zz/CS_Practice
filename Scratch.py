'''
Black Jack

class
Deck -
-data -vector of cards
-actions - draw, shuffle,
Cards
-data - string color, shape,
-action - set/get data members, look,

Players
-data - string name, vector of card hand
-action - draw deck, play card (Move), place one card face up, one card face down, give card to another player

Move
- data -
- action - put card on table, hit, don't hit
Game
- main driver class
- data - players, deck
- action - isWinnner, PlayerTurn,

Dealer (Players)
-
Inheritance
deck is a group of cards
dealer is a player

'''


class Solution:
    def all_comb(self, nums, rem, i, path, res):
        # base case
        if rem == 0:
            res.append(path)
            return

        # recursive case - i is less than nums
        for idx in range(i, len(nums)):
            if nums[idx] <= rem:
                path.append(nums[idx])
                self.all_comb(nums, rem - nums[idx], idx, path, res)
                path.pop()

    def combinationSum(self, candidates, target: int):
        res = []
        self.all_comb(candidates, target, 0, [], res)
        return res

nums = [2,3,6,7]
target = 7

sol = Solution()
print(sol.combinationSum(nums,target))


num = 145

print(num%10)

mult = 10

res = 0
pow = 0
while num:
    digit = num %10
    res += digit * (10 ** pow)
    # update
    pow += 1
    num //= 10

print(res)

res = [[] for _ in range(2)]
print(res)


res = [5,2]
res.sort()
print(res)
