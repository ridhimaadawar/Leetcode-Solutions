class Solution:
    def balanceBST(self, root):
        # Step 1: Inorder traversal to get sorted values
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Build balanced BST from sorted values
        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            node = TreeNode(vals[m])
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node

        return build(0, len(vals) - 1)
