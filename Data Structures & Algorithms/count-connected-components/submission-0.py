class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}

        num_comp = n

        for i in range(n):
            par[i] = i
            rank[i] = 0
        
        def find(x):
            p = par[x]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(x, y):
            nonlocal num_comp
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else: 
                par[p2] = p1
                rank[p1] +=  1
            num_comp -= 1
            return num_comp
        
        for i, j in edges:
            union(i, j)
        return num_comp
                 