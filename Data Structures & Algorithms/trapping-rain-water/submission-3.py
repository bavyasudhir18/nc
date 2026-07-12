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
                if maxL - height[l] > 0:
                    sum_trap += (maxL - height[l])
                maxL = max(maxL, height[l])
                
            else:
                r-=1
                if maxR - height[r] > 0:
                    sum_trap += (maxR - height[r])
                maxR = max(maxR, height[r])
            #print(sum_trap, maxL, maxR)
        return sum_trap 


