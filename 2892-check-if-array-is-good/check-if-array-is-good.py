from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        
        # Check length condition
        if len(nums) != n + 1:
            return False
        
        # Count frequencies
        freq = Counter(nums)
        
        # Check if numbers 1..n-1 appear exactly once, and n appears twice
        for i in range(1, n):
            if freq[i] != 1:
                return False
        
        return freq[n] == 2