from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # Special case: 1 -> 1^2 = 1
        if 1 in freq:
            ans = max(ans, freq[1] if freq[1] % 2 else freq[1] - 1)

        for x in freq:
            if x == 1:
                continue

            cur = x
            levels = 0

            while freq[cur] >= 2:
                nxt = cur * cur
                if freq.get(nxt, 0) == 0:
                    break
                levels += 1
                cur = nxt

            ans = max(ans, 2 * levels + 1)

        return ans