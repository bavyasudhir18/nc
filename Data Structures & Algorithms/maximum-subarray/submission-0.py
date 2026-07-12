class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0 
        for i in nums:
            if curSum + i < i:
                curSum = i
            else:
                curSum += i
            if curSum > maxSum:
                maxSum = curSum
        return maxSum