from heapq import heappush, heappop
from typing import List

class SparseTableRMQ:
    def __init__(self, data: List[int]):
        n = len(data)
        self.n = n
        self.max_log = n.bit_length() + 1

        self.f_max = [[0] * self.max_log for _ in range(n)]
        self.f_min = [[0] * self.max_log for _ in range(n)]

        self.lg = [0] * (n + 1)
        for i in range(2, n + 1):
            self.lg[i] = self.lg[i >> 1] + 1

        for i in range(n):
            self.f_max[i][0] = data[i]
            self.f_min[i][0] = data[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                self.f_max[i][j] = max(
                    self.f_max[i][j - 1],
                    self.f_max[i + length][j - 1]
                )
                self.f_min[i][j] = min(
                    self.f_min[i][j - 1],
                    self.f_min[i + length][j - 1]
                )
            j += 1

    def query_max(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return max(
            self.f_max[l][k],
            self.f_max[r - (1 << k) + 1][k]
        )

    def query_min(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return min(
            self.f_min[l][k],
            self.f_min[r - (1 << k) + 1][k]
        )


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SparseTableRMQ(nums)

        pq = []

        for l in range(n):
            val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
            heappush(pq, (-val, l, n - 1))

        ans = 0

        for _ in range(k):
            val, l, r = heappop(pq)
            ans += -val

            if r > l:
                nxt = st.query_max(l, r - 1) - st.query_min(l, r - 1)
                heappush(pq, (-nxt, l, r - 1))

        return ans