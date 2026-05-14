'''from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            for digit_char in str(num):
                result.append(int(digit_char))
        
        return result'''

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(d) for num in nums for d in str(num)]