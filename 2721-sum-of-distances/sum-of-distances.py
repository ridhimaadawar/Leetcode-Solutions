from collections import defaultdict

class Solution:
    def distance(self, nums):
        groups = defaultdict(list)

        # Step 1: group indices
        for i, num in enumerate(nums):
            groups[num].append(i)

        res = [0] * len(nums)

        # Step 2: process each group
        for indices in groups.values():
            prefix = [0] * (len(indices) + 1)

            # build prefix sum
            for i in range(len(indices)):
                prefix[i + 1] = prefix[i] + indices[i]

            total = len(indices)

            for i in range(total):
                curr = indices[i]

                # left side
                left = curr * i - prefix[i]

                # right side
                right = (prefix[total] - prefix[i + 1]) - curr * (total - i - 1)

                res[curr] = left + right

        return res