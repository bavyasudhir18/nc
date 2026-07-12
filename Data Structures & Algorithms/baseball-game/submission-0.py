class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in range(len(operations)):
            if operations[i]=="D":
                a.append(a[len(a)-1]*2)
            elif operations[i]=="C":
                a.pop()
            elif operations[i]=="+":
                a.append(a[len(a)-1]+a[len(a)-2])
            else:
                a.append(int(operations[i]))

        return sum(a)       