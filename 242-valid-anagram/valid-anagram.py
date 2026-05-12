class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # If lengths differ, cannot be anagrams
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Subtract counts using t
        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1

            if count[ch] < 0:
                return False

        return True