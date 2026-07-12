class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for i in range(len(matrix)):
            a = []
            s=0
            a.append(0)
            for j in range(len(matrix[0])):
                s+=matrix[i][j]
                a.append(s)
            self.prefix.append(a)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s=0
        for i in range(row1, row2+1):
            a=self.prefix[i][col2+1]
            a=a-self.prefix[i][col1]
            s+=a
        return s