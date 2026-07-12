class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visit=set()
        queue=deque()
        s=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    visit.add((i, j))
                    queue.append((i, j))
                elif grid[i][j]==1:
                    s+=1
        print(visit, queue, s)
        time=0

        if not visit and s==0:
            return 0

        while queue:
            for i in range(len(queue)):
                r, c=queue.popleft()
                p=[[-1, 0], [1, 0], [0, -1], [0, 1]]
                for m, n in p:
                    if min(r+m, c+n) >= 0 and r+m < rows and c+n < cols:
                        if grid[r+m][c+n]==1 and (r+m, c+n) not in visit:
                            s-=1
                            grid[r+m][c+n]=2
                            visit.add((r+m, c+n))
                            queue.append((r+m, c+n))
            time+=1
        if s>0:
            return -1
        return time-1
                