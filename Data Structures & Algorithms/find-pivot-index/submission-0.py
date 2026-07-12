class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suml =0
        sumr = sum(nums[1:])
        #print(suml, sumr)
        for i in range(1, len(nums)):
            if sumr == suml:
                return i-1
            suml += nums[i-1]
            sumr -= nums[i]
            #print(sumr, suml)
        if sumr == suml:
            return len(nums)-1
        return -1        