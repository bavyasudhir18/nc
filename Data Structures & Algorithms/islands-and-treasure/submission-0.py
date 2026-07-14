class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))
        level = 0
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while len(queue) > 0:
            level+=1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dir:
                    if (r+dr)<0 or (c+dc)<0 or (r+dr)>=rows or (c+dc)>=cols or (r+dr, c+dc) in visit or grid[r+dr][c+dc]==-1:
                        continue
                    grid[r+dr][c+dc] = level
                    visit.add((r+dr, c+dc))
                    queue.append((r+dr, c+dc))
                    
                    
                    
