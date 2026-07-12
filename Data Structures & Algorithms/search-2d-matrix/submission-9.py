class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l=0
        r=len(matrix)-1

        while l<=r:
            if target > matrix[l][0]:
                l+=1
            elif target < matrix[r][0]:
                r-=1
            else:
                return True

        n=r

        l=0
        r=len(matrix[n])-1

        while l<=r:
            m=r-(r-l)//2
            if target > matrix[n][m]:
                l=m+1
            elif target < matrix[n][m]:
                r=m-1
            else:
                return True
        return False


