from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        # Group indices by value for O(1) same-value jump lookups
        value_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_to_indices[val].append(i)

        visited = {0}
        queue = deque([(0, 0)])  # (index, steps)

        while queue:
            idx, steps = queue.popleft()

            # Generate all neighbors: left, right, and same-value indices
            neighbors = [idx - 1, idx + 1] + value_to_indices[arr[idx]]

            # Clear same-value group after processing to avoid re-visiting
            value_to_indices[arr[idx]].clear()

            for neighbor in neighbors:
                if neighbor == n - 1:
                    return steps + 1
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1