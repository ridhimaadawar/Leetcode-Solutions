# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):

            if not node:
                return

            # If leaf node
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return

            # Continue DFS
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")

        dfs(root, "")
        return result