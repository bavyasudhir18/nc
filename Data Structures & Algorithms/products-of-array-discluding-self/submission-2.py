class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[0]*len(nums)
        leftProd = [0] * len(nums)
        left = 1
        rightProd = [0] * len(nums)
        right = 1
        for i in range(len(nums)):
            left = left * nums[i]
            leftProd[i] = left
            right = right * nums[len(nums)-1-i]
            rightProd[len(nums)-1-i] = right
        # print(leftProd)
        # print(rightProd)
        for i in range(len(nums)):
            if i==0:
                a[0] = 1 * rightProd[i+1]
            if i==len(nums)-1:
                a[len(nums)-1] = 1 * leftProd[i-1]
            if i>0 and i<len(nums)-1:
                a[i] = rightProd[i+1] * leftProd[i-1]
            # print(a)
        return a

