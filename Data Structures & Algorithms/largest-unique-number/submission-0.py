class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        a=[]
        for i in f:
            if f[i]==1:
                a.append(i)
        if not a:
            return -1
        a=sorted(a)
        return a[-1]        