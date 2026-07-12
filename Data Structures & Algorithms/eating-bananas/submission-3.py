class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        
        res=max(piles)
        while l<=r:
            k=(l+r)//2
            s=0
            for pile in piles:
                s=s+(math.ceil(pile/k))
            if s<=h:
                res=min(res, k)
                r=k-1
            else:
                l=k+1
        return res