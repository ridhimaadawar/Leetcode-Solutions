class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # reverse whole array
        reverse(0, n - 1)
        # reverse first k elements
        reverse(0, k - 1)
        # reverse remaining elements
        reverse(k, n - 1)
