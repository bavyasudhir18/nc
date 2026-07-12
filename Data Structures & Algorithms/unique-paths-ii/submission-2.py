class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid 
        m = len(grid)
        n = len(grid[0])

        dp = [0]*n
        print(dp)
        dp[n-1]=1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j]==1:
                    dp[j]=0
                elif j+1 < n:
                    dp[j] = dp[j] + dp[j+1]
            #print(dp)
        return dp[0]