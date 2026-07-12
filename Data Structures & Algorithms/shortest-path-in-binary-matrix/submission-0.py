class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows=len(grid)
        cols=len(grid[0])

        if grid[rows-1][cols-1]==1 or grid[0][0]==1:
            return -1

        #length=0
        visit=set()
        queue=deque()
        visit.add((0, 0))
        queue.append((0, 0))
        length=0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r==rows-1 and c==cols-1:
                    return length+1

                a=[[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
                for dr, dc in a:
                    if min(r+dr, c+dc) < 0 or (r+dr)>=rows or (c+dc)>=cols or (r+dr, c+dc) in visit or grid[r+dr][c+dc]==1:
                        continue
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))
            length+=1
        return -1


        