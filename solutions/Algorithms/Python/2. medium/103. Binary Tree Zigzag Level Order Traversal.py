# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
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
        return [res[i] if i % 2 != 0 else res[i][::-1] for i in range(len(res))]