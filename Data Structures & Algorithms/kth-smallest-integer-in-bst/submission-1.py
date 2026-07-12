# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        n=0
        def inorder(node, n):
            if not node:
                return
            inorder(node.left, n)
            res.append(node.val)
            n+=1
            if n==k:
                return node.val
            inorder(node.right, n)
        inorder(root, n)
        return res[k-1]