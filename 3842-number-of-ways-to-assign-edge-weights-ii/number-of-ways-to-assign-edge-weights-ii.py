from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1

        # Build tree
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Binary lifting preprocessing
        LOG = (n).bit_length()
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        q = deque([1])
        parent = [0] * (n + 1)
        parent[1] = 0

        while q:
            u = q.popleft()
            for v in g[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)

        for i in range(1, n + 1):
            up[0][i] = parent[i]

        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[j][i] = up[j - 1][up[j - 1][i]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            bit = 0
            while diff:
                if diff & 1:
                    a = up[bit][a]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]

            return up[0][a]

        # powers of 2 modulo MOD
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []

        for u, v in queries:
            w = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[w]

            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow2[dist - 1])

        return ans