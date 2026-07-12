class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min=val
        else:
            a=val-self.min
            self.stack.append(a)
            if self.min > val:
                self.min = val
        

    def pop(self) -> None:
        if not self.stack:
            return
        p=self.stack.pop()
        if p<0:
            self.min= self.min - p
        
    def top(self) -> int:
        top=self.stack[-1]
        if top > 0:
            return top +self.min
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
        
