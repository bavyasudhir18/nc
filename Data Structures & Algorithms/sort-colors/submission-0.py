class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        a=[0,0,0]
        for i in range(len(nums)):
            a[nums[i]]+=1
        print(a)
        k=0
        for i in range(len(a)):
            for j in range(a[i]):
                nums[k]=i
                k=k+1
        return nums