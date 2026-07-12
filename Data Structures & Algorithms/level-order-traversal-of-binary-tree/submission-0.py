# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        if root:
            queue.append(root)
        b=[]
        while len(queue)>0:
            a=[]
            for i in range(len(queue)):
                cur=queue.popleft()
                a.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            b.append(a)
        return b

