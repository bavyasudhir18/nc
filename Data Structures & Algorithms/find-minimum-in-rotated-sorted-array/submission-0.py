class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        k=1
        k=k%len(nums)
        for i in range(len(nums)):
            if nums[0]>nums[1]:
                return nums[1]
            nums=nums[-k:]+nums[:-k]