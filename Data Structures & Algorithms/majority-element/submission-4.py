class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        
        a=[]
        
        for i in f:
            if f[i]>len(nums)//2:
                return i
        
        
 

