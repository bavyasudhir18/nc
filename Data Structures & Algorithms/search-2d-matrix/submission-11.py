class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])

        l=0
        r=rows*cols-1

        print(l, r)

        while l<=r:
            m=r-(r-l)//2
            row=m//cols
            col=m%cols
            if target > matrix[row][col]:
                l=m+1
            elif target < matrix[row][col]:
                r=m-1
            else:
                return True
        return False