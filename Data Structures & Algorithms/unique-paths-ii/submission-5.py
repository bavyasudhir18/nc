class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 and grid[rows-1][cols-1]==1:
            return 0
        
        grid[rows-1][cols-1]=1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r==rows-1 and c==cols-1:
                    continue
                if grid[r][c]==1:
                    grid[r][c]=0
                else:
                    if r+1 < rows:
                        down = grid[r+1][c]
                    else:
                        down=0
                    if c+1 < cols:
                        right = grid[r][c+1]
                    else:
                        right=0
                    
                    grid[r][c] += (down + right)
        return grid[0][0]