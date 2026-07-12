
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        t=image[sr][sc]
        return self.dfs(image, sr, sc, color, t)
    
    def dfs(self,image, r, c, color, t):
        rows=len(image)
        cols=len(image[0])

        if min(r,c)<0 or r==rows or c==cols or image[r][c]!=t:
            return

        image[r][c]=color

        self.dfs(image, r+1, c, color, t)
        self.dfs(image, r-1, c, color, t)
        self.dfs(image, r, c+1, color, t)
        self.dfs(image, r, c-1, color, t)
     
        return image
             