class Solution(object):
    def binary_search(self, nums, target, l, r):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if l == r:
                break  # covers decimals
            elif target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1

        return -1

    def search(self, nums, target):
        if len(nums) < 1: return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # both sides sorted
            if nums[l] <= nums[mid] <= nums[r]:
                return self.binary_search(nums, target, l, r)

            # left side sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    return self.binary_search(nums, target, l, mid)
                else:
                    l = mid + 1

            # right side sorted
            elif nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    return self.binary_search(nums, target, mid, r)
                else:
                    r = mid - 1

        return -1
sol = Solution()
print(sol.search([5,1,3],5))