# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        
        prev = None

        slow = head
        fast = head
        length = 0

        while fast and fast.next:
            length += 1
            slow = slow.next
            fast = fast.next.next
        
        length1 = length

        while length1 > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            length1-=1

        max_twin_sum = 0
    
        while slow:
            max_twin_sum = max (max_twin_sum, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return max_twin_sum       