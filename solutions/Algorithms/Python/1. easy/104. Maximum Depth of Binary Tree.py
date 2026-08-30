# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    if root:
        return max(maxDepth(root.left) + 1, maxDepth(root.right) + 1) 
    return 0

