class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=set()
        t1=set()

        for i in range(len(s)):
            s1.add(s[i])
        for i in range(len(t)):
            t1.add(t[i])
        
        f1={}
        f2={}

        for i in s:
            if i in f1:
                f1[i]+=1
            else:
                f1[i]=1
        
        for i in t:
            if i in f2:
                f2[i]+=1
            else:
                f2[i]=1
        
        if f1==f2:
            return True
        else:
            return False