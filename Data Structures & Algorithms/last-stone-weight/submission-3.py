class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=sorted(stones)
        while len(stones)>1:
            a=stones.pop()
            b=stones.pop()
            if a!=b:
                res=abs(a-b)
                stones.append(res)
                stones=sorted(stones)
        if len(stones)==1:
            return stones[0]
        return 0