class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}

        for i, j in edges:
            par[i], par[j] = i, j
            rank[i], rank[j] = 0, 0
        
        def find(x):
            p = par[x]
            while p != par[p]:
                par[p] = par[par[p]]
                p=par[p]
            return p
        
        for (i, j) in edges:
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return [i, j]
            if rank[p1] > rank[p2]:
                par[p2] = p1
            if rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p1] += 1