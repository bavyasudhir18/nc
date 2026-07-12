class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=l=0
        while i<len(s):
            if s[i]==" ":
                while i<len(s) and s[i]==" ":
                    i+=1
                if i==len(s):
                    return l
                l=0
            else:
                i+=1
                l+=1
        return l

        