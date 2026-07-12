class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        i=0
        maxLeft = []
        ml = 0
        maxRight = []
        mr = 0
        while i < len(height):
            ml = max(ml, height[i])
            maxLeft.append(ml)
            mr = max(mr, height[len(height)-i-1])
            maxRight.append(mr)
            i+=1
        maxRight = maxRight[::-1]
        i=0
        sum_water_trapped = 0
        while i < len(height):
            indivi_trap_water = min(maxLeft[i], maxRight[i]) - height[i]
            if indivi_trap_water > 0:
                sum_water_trapped += indivi_trap_water
            i+=1

        return sum_water_trapped       