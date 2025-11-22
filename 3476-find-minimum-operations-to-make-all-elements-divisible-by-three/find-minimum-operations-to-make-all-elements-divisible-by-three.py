class Solution:
    def minimumOperations(self, nums):
        ops = 0
        for x in nums:
            r = x % 3
            ops += min(r, 3 - r)
        return ops
