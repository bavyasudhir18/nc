class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        a=[]
        for i in range(len(s)):
            if (ord(s[i])>=97 and ord(s[i])<=122 ):
                a.append(ord(s[i]))
            elif (ord(s[i])>=65 and ord(s[i])<=90):
                a.append(ord(s[i])+32)
            elif (ord(s[i])>=48 and ord(s[i])<=57):
                a.append(ord(s[i]))
        print(a)
        l=0
        r=len(a)-1
        print(r)
        m=0
        while l<=r:
            if a[l]!=a[r]:
                m=m+1
            l=l+1
            r=r-1
        print(m)

        if m==0:
            return True
        return False

        