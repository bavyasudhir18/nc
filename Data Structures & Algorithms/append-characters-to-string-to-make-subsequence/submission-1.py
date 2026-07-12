class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m=0
        n=0
        for i in range(len(s)):
            if n==len(t):
                break
            if s[i]==t[n]:
                m=m+1
                n=n+1
            else:
                m=0
        if m < len(t):
            return len(t)-n
        else:
            return 0

               