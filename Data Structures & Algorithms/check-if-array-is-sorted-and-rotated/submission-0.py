class Solution:
    def check(self, nums: List[int]) -> bool:
        n=sorted(nums)
        for i in range(len(nums)):
            if n==nums:
                return True
            nums=nums[1:] + nums[:1]
        return False
        