class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p={}
        for i, num in enumerate(nums):
            p[num]=i
        print(p)
        for i, num in enumerate(nums):
            print(i, num)
            diff=target-num
            if diff in p and p[diff]!=i:
                return[i, p[diff]]
        return[]
        