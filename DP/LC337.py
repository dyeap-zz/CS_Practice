class Solution:
    cache = {}

    def max_rob(self, root, prev_rob):
        cache = self.cache
        if (root, prev_rob) in cache: return cache[(root, prev_rob)]
        # base case
        if root is None: return 0
        # root is valid house to rob
        nottaken = self.max_rob(root.left, 0) + self.max_rob(root.right, 0)
        if prev_rob:
            take = nottaken
        else:
            take = root.val + self.max_rob(root.left, 1) + self.max_rob(root.right, 1)

        cache[(root, prev_rob)] = max(take, nottaken)
        return max(take, nottaken)

    def rob(self, root) -> int:
        return self.max_rob(root, 0)