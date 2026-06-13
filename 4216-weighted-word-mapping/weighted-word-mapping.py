from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            total = sum(weights[ord(c) - ord('a')] for c in word)
            ans.append(chr(ord('z') - (total % 26)))

        return ''.join(ans)