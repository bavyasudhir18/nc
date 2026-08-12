class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        f = {}
        s=sorted(s)
        g=sorted(g)
        for i in s:
            if i not in f:
                f[i] = 1
            else:
                f[i] += 1
        print(f)
        for i in g:
            for j in f:
                if j>=i and f[j]>0:
                    f[j]-=1
                    res += 1
                    break
        return res        