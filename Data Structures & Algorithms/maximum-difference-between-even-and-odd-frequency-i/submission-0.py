class Solution:
    def maxDifference(self, s: str) -> int:
        f = {}
        for i in s:
            if i not in f:
                f[i] = 1
            else:
                f[i] += 1
        
        e=[]
        o=[]
        for i in f:
            if f[i]%2==0:
                e.append(f[i])
            else:
                o.append(f[i])
        
        max_odd = max(o)
        min_even = min(e)
        return max_odd - min_even        