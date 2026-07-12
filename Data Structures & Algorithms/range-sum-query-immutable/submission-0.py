class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        s=0
        for i in nums:
            s+=i
            self.prefix.append(s)
        

    def sumRange(self, left: int, right: int) -> int:
        s = self.prefix[right]
        s_2 = self.prefix[left-1] if left>0 else 0
        return s-s_2
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)