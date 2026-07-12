class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m=1
        for i in range(k%len(nums)):
            nums[:]=nums[-m:]+nums[:-m]
  