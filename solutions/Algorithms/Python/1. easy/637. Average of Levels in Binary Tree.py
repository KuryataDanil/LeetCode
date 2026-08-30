from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        if not root:
            return []
        res = []
        def dfs(node, level):
            if not node:
                return
            print(res)
            if len(res) - 1 < level:
                res.append([node.val])
            else:
                res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            return
        dfs(root, 0)
        return [sum(i) / len(i) for i in res]
