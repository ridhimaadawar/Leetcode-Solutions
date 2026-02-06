class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        left = 0
        max_len = 0

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len
