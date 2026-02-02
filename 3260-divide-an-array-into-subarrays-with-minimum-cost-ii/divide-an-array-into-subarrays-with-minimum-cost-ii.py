from bisect import bisect_left, insort

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        need = k - 1
        res = float("inf")

        window = []
        window_sum = 0
        left = 1

        for right in range(1, n):
            # add nums[right]
            insort(window, nums[right])
            if len(window) <= need:
                window_sum += nums[right]
            else:
                if nums[right] < window[need]:
                    window_sum += nums[right]
                    window_sum -= window[need]

            # shrink window if too large
            while right - left > dist:
                x = nums[left]
                idx = bisect_left(window, x)

                if idx < need:
                    window_sum -= x
                    if len(window) > need:
                        window_sum += window[need]
                window.pop(idx)
                left += 1

            if len(window) >= need:
                res = min(res, window_sum)

        return nums[0] + res
