class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        l = 0
        s = 0
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                length=min(length, r-l+1)
                s-=nums[l]
                l+=1
            
        return 0 if length == float("inf") else length     