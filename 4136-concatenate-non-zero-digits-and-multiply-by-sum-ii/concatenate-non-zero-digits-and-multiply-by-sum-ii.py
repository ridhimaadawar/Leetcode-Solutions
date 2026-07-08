from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        k = len(digits)

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefVal = [0] * (k + 1)
        prefSum = [0] * (k + 1)

        for i, d in enumerate(digits):
            prefVal[i + 1] = (prefVal[i] * 10 + d) % MOD
            prefSum[i + 1] = prefSum[i] + d

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1
            x = (prefVal[right + 1] - prefVal[left] * pow10[length]) % MOD
            digit_sum = prefSum[right + 1] - prefSum[left]

            ans.append((x * digit_sum) % MOD)

        return ans