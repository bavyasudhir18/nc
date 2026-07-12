class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min = val
        else:
            if val < self.min:
                a = 2*val - self.min
                self.stack.append(a)
                self.min = val
            else:
                self.stack.append(val)
        

    def pop(self) -> None:
        if not self.stack:
            return
        pop=self.stack.pop()
        if pop < self.min:
            self.min = 2*self.min - pop
        if not self.stack:
            self.min= None
        

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            if self.stack[-1]<self.min:
                return self.min
            else:
                return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
