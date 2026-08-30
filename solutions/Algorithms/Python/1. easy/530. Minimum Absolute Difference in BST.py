# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        arr = []

        def bfs(node):
            if not node:
                return
            bfs(node.left)
            arr.append(node.val)
            bfs(node.right)

        bfs(root)
        absmin = 100000000000000000000
        print(arr)
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) < absmin:
                absmin = abs(arr[i] - arr[i + 1])
        return absmin
