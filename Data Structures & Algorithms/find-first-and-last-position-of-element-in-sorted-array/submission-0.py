class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target < nums[m]:
                r=m-1
                print("l, nums[l]", nums[l])
            elif target > nums[m]:
                l=m+1
            else:
                a=[]
                for i in range(l, r+1):
                    if nums[i]==target:
                        a.append(i)
                return [a[0], a[-1]]

        return [-1, -1]        