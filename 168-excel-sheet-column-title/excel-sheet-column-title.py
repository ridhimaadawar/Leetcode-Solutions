class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1  # shift to 0-based indexing
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return ''.join(reversed(result))