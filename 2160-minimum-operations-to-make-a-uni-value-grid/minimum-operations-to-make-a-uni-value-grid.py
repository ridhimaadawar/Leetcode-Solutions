from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid
        arr = [num for row in grid for num in row]
        
        # Check feasibility: all elements must have same remainder mod x
        rem = arr[0] % x
        for num in arr:
            if num % x != rem:
                return -1
        
        # Normalize values by dividing by x
        arr = [num // x for num in arr]
        
        # Sort and pick median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Compute minimum operations
        operations = 0
        for num in arr:
            operations += abs(num - median)
        
        return operations