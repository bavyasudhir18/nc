class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=len(word1)
        n=len(word2)
        s=""
        if m<n:
            for i in range(len(word1)):
                s+=word1[i]
                s+=word2[i]
                k=i
            s+=word2[k+1:]
        else:
            for i in range(len(word2)):
                s+=word1[i]
                s+=word2[i]
                k=i
            s+=word1[k+1:]
        return s