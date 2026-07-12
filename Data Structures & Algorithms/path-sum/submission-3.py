# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, s):
            if not node:
                return False
            s+=node.val
            if not node.left and not node.right:
                return s==targetSum
            return dfs(node.right, s) or dfs(node.left, s)
        s=0
        return dfs(root, s)