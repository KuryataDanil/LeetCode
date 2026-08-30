# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p and q:
        return p.val == q.val and isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
    return not p and not q
        
