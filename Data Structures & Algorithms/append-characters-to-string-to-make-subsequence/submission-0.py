class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sa=[]
        for i in s:
            sa.append(i)
        ta=[]
        for i in t:
            ta.append(i)
        m=0
        n=0
        for i in range(len(sa)):
            if n==len(ta):
                break
            if sa[i]==ta[n]:
                m=m+1
                n=n+1
            else:
                m=0
        if m < len(ta):
            return len(ta)-n
        else:
            return 0

               