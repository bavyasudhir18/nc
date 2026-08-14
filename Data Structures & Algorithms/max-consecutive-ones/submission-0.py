class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=0
        res = 0
        for i in nums:
            if i==1:
                s+=1
            else:
                res = max(res, s)
                s=0
        res = max(res, s)
        return res