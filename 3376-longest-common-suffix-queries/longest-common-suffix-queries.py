from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        root = TrieNode()

        # Returns True if idx1 is a better candidate than idx2
        def better(idx1, idx2):
            if idx2 == -1:
                return True
            
            l1 = len(wordsContainer[idx1])
            l2 = len(wordsContainer[idx2])

            if l1 != l2:
                return l1 < l2

            return idx1 < idx2

        # Build trie using reversed words
        for i, word in enumerate(wordsContainer):
            node = root

            # update root candidate
            if better(i, node.best_idx):
                node.best_idx = i

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if better(i, node.best_idx):
                    node.best_idx = i

        ans = []

        # Process queries
        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.best_idx)

        return ans