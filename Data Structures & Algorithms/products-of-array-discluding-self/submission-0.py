class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            p=1
            for j in range(len(nums)):
                if i!=j:
                    p=p*nums[j]
            a.append(p)
        return a
