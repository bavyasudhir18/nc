class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p={}
        for i,n in enumerate(nums):
            d=target-n
            if d in p:
                return [p[d], i]
            p[n]=i
        return[]
        