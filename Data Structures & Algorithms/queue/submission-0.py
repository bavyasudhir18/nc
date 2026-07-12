class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev

class Deque:
    
    def __init__(self):
        self.head=ListNode(0)
        self.tail=ListNode(0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def isEmpty(self) -> bool:
        if self.head.next==self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        node=ListNode(value)
        if self.isEmpty():
            self.head.next=node
            self.tail.prev=node
            node.next=self.tail
            node.prev=self.head
            return
        cur=self.tail.prev
        self.tail.prev=node
        cur.next=node
        node.next=self.tail
        node.prev=cur
        return


    def appendleft(self, value: int) -> None:
        if self.isEmpty():
            node=ListNode(value)
            self.head.next=node
            self.tail.prev=node
            node.next=self.tail
            node.prev=self.head
            return            
        node=ListNode(value)
        cur=self.head.next
        self.head.next=node
        cur.prev=node
        node.prev=self.head
        node.next=cur
        return

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        cur=self.tail.prev
        self.tail.prev=self.tail.prev.prev
        self.tail.prev.next=self.tail
        return cur.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        cur=self.head.next
        self.head.next=self.head.next.next
        self.head.next.prev=self.head
        return cur.val
        
