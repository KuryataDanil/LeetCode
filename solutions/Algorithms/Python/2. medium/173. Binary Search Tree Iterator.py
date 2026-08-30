# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = []

        def dfs(node: TreeNode):
            if node is None:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)

        dfs(root)
        self.index = -1
        self.length = len(self.arr)

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < self.length
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
