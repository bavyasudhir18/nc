class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        f={}
        for i in nums:
            if i not in f:
                f[i]=1
            else:
                return True
        return False