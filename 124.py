# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = float('-inf')
        def dfs(root):
            if not root: return 0
            self.maxsum = max(self.maxsum, dfs(root.left) + dfs(root.right) + root.val)
            return max(0, max(dfs(root.left), dfs(root.right)) + root.val)
        dfs(root)
        return self.maxsum
