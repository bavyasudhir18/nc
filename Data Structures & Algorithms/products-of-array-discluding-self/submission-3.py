class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        a=[1]*len(nums)
        for i in range(len(nums)):
            a[i] = a[i] * left
            a[len(a)-i-1] = a[len(a)-i-1] * right
            left = left * nums[i]
            right = right * nums[len(nums)-i-1] 
            #print(left, right, a)
        return a 