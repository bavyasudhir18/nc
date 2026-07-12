class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height=sorted(heights)
        s=0
        for i in range(len(heights)):
            if heights[i]!=sorted_height[i]:
                s+=1
        return s       