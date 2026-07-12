
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, r, c):
            if min(r, c)<0 or r==rows or c==cols or grid[r][c]==0:
                return 0
            grid[r][c]=0

            return 1 + dfs(grid, r+1, c) + dfs(grid, r-1, c) + dfs(grid, r, c-1) + dfs(grid, r, c+1)
        
        max_area=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    a=dfs(grid, i, j)
                    print(a)
                    max_area=max(max_area, a)
        return max_area