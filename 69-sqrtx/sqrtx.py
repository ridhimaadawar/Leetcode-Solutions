class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid <= x // mid:
                left = mid + 1
            else:
                right = mid - 1
        return right

sol = Solution()
x = 8
print(sol.mySqrt(x))