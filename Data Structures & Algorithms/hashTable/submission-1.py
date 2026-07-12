class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.table = [None]*self.capacity
    
    def hash_function(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev=None
            while node:
                if node.key == key:
                    node.value = value
                    return    
                prev=node
                node=node.next
            prev.next=Node(key, value)
            self.size +=1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node=node.next
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index]=node.next
                self.size -= 1
                return True
            prev=node
            node=node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newTable = [None] * self.capacity
        for node in self.table:
            while node:
                index = node.key % self.capacity
                if newTable[index] is None:
                    newTable[index]=Node(node.key, node.value)
                else:
                    head=newTable[index]
                    node.next=head
                    newTable[index] = node
                node = node.next
        self.table = newTable


