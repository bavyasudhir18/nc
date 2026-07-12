class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    
    def helper(self, nums):
        rob1=0
        rob2=0
        for i in nums:
            newRob = max(rob1 + i, rob2)
            rob1=rob2
            rob2=newRob
        return rob2

        