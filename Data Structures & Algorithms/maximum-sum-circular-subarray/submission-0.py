class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax = nums[0]
        globalmin = nums[0]

        curmax = 0
        curmin = 0

        total = 0

        for i in nums:
            if curmax + i < i:
                curmax = i
            else:
                curmax += i

            if curmin + i < i:
                curmin = curmin + i
            else:
                curmin = i
            
            if curmax > globalmax:
                globalmax = curmax
            if curmin < globalmin:
                globalmin = curmin
            
            total += i

            #print(curmax, globalmax, curmin, globalmin)
        
        if globalmax < 0:
            return globalmax
        else:
            return globalmax if globalmax > (total - globalmin) else (total - globalmin)        