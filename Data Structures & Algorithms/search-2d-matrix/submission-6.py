class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        print(r)
        c=len(matrix[0])
        print(c)

        r_=0
        c_=c-1

        while r_<r and c_>=0:
            print(r_, c_)
            if matrix[r_][c_]>target:
                c_-=1
            elif matrix[r_][c_]<target:
                r_+=1
            else:
                return True

        return False