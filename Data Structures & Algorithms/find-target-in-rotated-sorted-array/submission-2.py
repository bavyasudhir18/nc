class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[0]!=target:
                k+=1
                nums=nums[1:]+nums[:1]
            else:
                return k
        return -1
        
