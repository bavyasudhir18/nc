class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0
        prefix = {0: 1}
        for i in nums:
            cursum += i
            diff = cursum - k
             
            if diff in prefix:
                res+=prefix[diff]
            
            if cursum not in prefix:
                prefix[cursum] = 1
            else:
                prefix[cursum] += 1
        return res