# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(lists)
        node=[]
        for lst in lists:
            while lst:
                node.append(lst.val)
                lst=lst.next
        print(node)
        node=sorted(node)
        print(node)

        res=ListNode(0)
        cur=res
        for n in node:
            cur.next=ListNode(n)
            cur=cur.next
        return res.next