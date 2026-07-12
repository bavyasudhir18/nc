class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            a=heapq.heappop(stones) 
            b=heapq.heappop(stones)
            if a!=b:
                res=(a - b)
                heapq.heappush(stones, res)
            if a==b:
                res=0
                heapq.heappush(stones, res)
        return -stones[0]