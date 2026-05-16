class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping:              # it's a closing bracket
                if not stack:                # nothing to match with
                    return False
                top = stack.pop()
                if top != mapping[char]:     # mismatched bracket
                    return False
            else:
                stack.append(char)           # it's an opening bracket, push it

        return len(stack) == 0              # valid only if nothing is left over