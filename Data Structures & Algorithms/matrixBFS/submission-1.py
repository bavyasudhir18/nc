class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q=deque()
        visit=set()

        q.append([0,0])
        visit.add((0,0))

        dir=[[1, 0], [-1, 0], [0, 1], [0, -1]]

        s=0

        while q:
            for i in range(len(q)):
                r, c=q.popleft()

                if r==rows-1 and c==cols-1:
                    return s

                for dr, dc in dir:
                    row=r+dr
                    col=c+dc
                    if min(row, col)<0 or row==rows or col==cols or (row, col) in visit:
                        continue
                    if grid[row][col]==0:
                        visit.add((row, col))
                        q.append((row, col))
            s+=1
        return -1

        