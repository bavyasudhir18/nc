class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxL = height[0]
        maxR = height[len(height)-1]
        sum_trap = 0
        while l<r:
            if maxL <= maxR:
                l+=1
                maxL = max(maxL, height[l])
                sum_trap += (maxL - height[l])
                
            else:
                r-=1
                maxR = max(maxR, height[r])
                sum_trap += (maxR - height[r])
            #print(sum_trap, maxL, maxR)
        return sum_trap 


