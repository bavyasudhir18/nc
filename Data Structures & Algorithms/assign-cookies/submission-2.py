class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        f = {}
        s=sorted(s)
        g=sorted(g)
        l = 0
        r = 0

        while r<len(s) and l<len(g):
            if s[r] >= g[l]:
                res+=1
                r+=1
                l+=1
            else:
                r+=1
        return res