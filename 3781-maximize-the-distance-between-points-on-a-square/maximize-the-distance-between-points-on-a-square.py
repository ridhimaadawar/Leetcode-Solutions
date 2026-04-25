import bisect

class Solution(object):
    def maxDistance(self, side, points, k):

        def get_pos(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y

        # map to perimeter
        arr = sorted(get_pos(x, y) for x, y in points)
        n = len(arr)
        L = 4 * side

        # extend for circular
        arr_ext = arr + [x + L for x in arr]

        def can(d):
            for i in range(n):
                cnt = 1
                cur = arr_ext[i]

                while cnt < k:
                    # jump to next >= cur + d
                    nxt = bisect.bisect_left(arr_ext, cur + d)

                    if nxt >= i + n:
                        break

                    cur = arr_ext[nxt]
                    cnt += 1

                if cnt == k:
                    # check wrap-around distance
                    if arr_ext[i] + L - cur >= d:
                        return True

            return False

        left, right = 0, 2 * side
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans