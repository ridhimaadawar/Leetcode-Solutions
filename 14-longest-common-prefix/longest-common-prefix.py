'''class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for other in strs[1:]:
                if i >= len(other) or other[i] != char:
                    print("Mismatch found at word '{}', index {}".format(other, i))
                    return strs[0][:i]

        return strs[0]'''

class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return""
        return prefix