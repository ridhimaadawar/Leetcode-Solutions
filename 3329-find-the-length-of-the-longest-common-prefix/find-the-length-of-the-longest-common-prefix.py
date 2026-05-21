class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefix_set = set()

        # Store all prefixes of arr1 elements
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefix_set.add(s[:i])   # e.g. "1", "12", "123"

        max_len = 0

        # Check all prefixes of arr2 elements against the set
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in prefix_set:
                    max_len = max(max_len, i)

        return max_len