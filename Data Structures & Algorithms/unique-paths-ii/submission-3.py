class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid

        a=[[0, 0, 0],[0, 0, 0]]

        rows= len(grid)
        cols =len(grid[0])

        dp = [[0]*(cols+1) for _ in range(rows+1)]
        
        dp[rows-1][cols-1]=1
        #print(dp)

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if grid[r][c] == 1:
                    dp[r][c]=0
                else:
                    dp[r][c] += (dp[r+1][c] + dp[r][c+1])
            #print(dp)
        
        return dp[0][0]