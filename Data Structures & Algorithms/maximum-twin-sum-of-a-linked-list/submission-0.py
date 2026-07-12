# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=head
        a=[]
        while res:
            a.append(res.val)
            res=res.next
        cur=head
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        b=[]
        while prev:
            b.append(prev.val)
            prev=prev.next
        c=[]
        for i in range(len(a)//2):
            c.append(a[i]+b[i])
        if c:
            return max(c)
        return []