class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        a=[]
        for i in strs:
            a.append(len(i))
        m=-1
        for i in range(min(a)):
            r=0
            for j in range(len(strs)):
                if strs[0][i]==strs[j][i]:
                    r+=1
            if r==len(strs):
                s+=strs[0][i]
            elif r!=len(strs):
                return s
        return s