# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, num: int) -> int:
            if not node:
                return 0
            if node.left is None and node.right is None:
                return num * 10 + node.val
            return dfs(node.left, num * 10 + node.val) + dfs(node.right, num * 10 + node.val)

        return int(dfs(root, 0))
