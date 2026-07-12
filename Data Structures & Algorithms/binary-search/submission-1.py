class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(0, len(nums)-1, nums, target)
    
    def binarysearch(self, l, r, nums, target):
        if l>r:
            return -1
        m=(l+r)//2
        if nums[m]<target:
            return self.binarysearch(m+1, r, nums, target)
        elif nums[m]>target:
            return self.binarysearch(l, m-1, nums, target)
        else:
            return m
    