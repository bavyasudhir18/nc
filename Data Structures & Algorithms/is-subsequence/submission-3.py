class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        if len(s)==0:
            return True
        while r < len(t):
            if l == len(s)-1:
                return True
            if s[l] == t[r]:
                l+=1
                r+=1
            else:
                r+=1
        return False