class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}

        for c1, c2 in zip(s, t):

            # Check mapping from s -> t
            if c1 in map_st:
                if map_st[c1] != c2:
                    return False
            else:
                map_st[c1] = c2

            # Check mapping from t -> s
            if c2 in map_ts:
                if map_ts[c2] != c1:
                    return False
            else:
                map_ts[c2] = c1

        return True