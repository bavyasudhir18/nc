class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = deque()
        visit=set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    queue.append((i, j))
                    visit.add((i, j))
                    break
            if len(queue)==1:
                break


        dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        

        while len(queue) > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for m, n in dire:
                    dr = r + m
                    dc = c + n
                    if dr < 0 or dc < 0 or dr >= len(grid) or dc >= len(grid[0]) or grid[dr][dc] == 0:
                        res += 1
                    elif (grid[dr][dc] == 1 and (dr, dc) not in visit):
                        queue.append((dr, dc))
                        visit.add((dr, dc))
        return res       