# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        t=head
        prev=None

        cur1=head
        s=0
        while cur1:
            s+=1
            cur1=cur1.next
        
        k=k%s

        while k>0:

            while cur.next:
                prev = cur
                cur=cur.next    
            prev.next = None
            cur.next = t

            t = cur
            k-=1
        return cur        