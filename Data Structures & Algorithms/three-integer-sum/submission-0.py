class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        b=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    a=[]
                    if i!=j and j!=k and k!=i:
                        a=[]
                        if nums[i]+nums[j]+nums[k]==0:
                                a.append(nums[i])
                                a.append(nums[j])
                                a.append(nums[k])
                        if a:
                            if sorted(a) not in b:
                                b.append(sorted(a))
        return b     