# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def leafPath(root, path, targetSum):
            if not root :
                return False
            path.append(root.val)
            s=sum(path)
            if not root.left and not root.right:
                if targetSum==s:
                    return True
            if leafPath(root.left, path, targetSum):
                return True
            if leafPath(root.right, path, targetSum):
                return True
            path.pop()
            return False
        path=[]
        return leafPath(root, path, targetSum)
