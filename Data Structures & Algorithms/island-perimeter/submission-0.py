class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    for r, c in dire:
                        dr = i + r
                        dc = j + c
                        if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[0]):
                            if grid[dr][dc] == 0:
                                res+=1
                        else:
                            res += 1
        return res        