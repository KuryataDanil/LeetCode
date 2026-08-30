# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst_helper(root, float('-inf'), float('inf'))

    def is_valid_bst_helper(self, node, lower_limit, upper_limit):
        if not node:
            return True

        if not (lower_limit < node.val < upper_limit):
            return False

        return (self.is_valid_bst_helper(node.left, lower_limit, node.val) and
                self.is_valid_bst_helper(node.right, node.val, upper_limit))
