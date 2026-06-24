class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1
        size = 2 * m

        # state:
        # 0..m-1     -> U
        # m..2m-1    -> D

        T = [[0] * size for _ in range(size)]

        # D -> U
        for y in range(m):
            for x in range(y):
                T[y][m + x] = 1

        # U -> D
        for y in range(m):
            for x in range(y + 1, m):
                T[m + y][x] = 1

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]

            for i in range(n):
                for k in range(n):
                    if A[i][k] == 0:
                        continue

                    a = A[i][k]

                    for j in range(n):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + a * B[k][j]) % MOD

            return C

        def mat_pow(M, p):
            n = len(M)

            R = [[0] * n for _ in range(n)]
            for i in range(n):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(M, R)

                M = mat_mul(M, M)
                p >>= 1

            return R

        def mat_vec_mul(M, v):
            n = len(M)
            res = [0] * n

            for i in range(n):
                s = 0
                row = M[i]

                for j in range(n):
                    if row[j]:
                        s += row[j] * v[j]

                res[i] = s % MOD

            return res

        # Length = 2 initialization
        init = [0] * size

        for y in range(m):
            init[y] = y              # U[y]
            init[m + y] = m - 1 - y  # D[y]

        P = mat_pow(T, n - 2)

        final_state = mat_vec_mul(P, init)

        return sum(final_state) % MOD