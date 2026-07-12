class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for i in nums:
            for j in res:
                res = res + [j + [i]]
        return res