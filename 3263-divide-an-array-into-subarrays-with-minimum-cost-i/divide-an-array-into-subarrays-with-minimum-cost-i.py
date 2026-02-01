class Solution:
    def minimumCost(self, nums):
        rest = nums[1:]
        rest.sort()
        return nums[0] + rest[0] + rest[1]
