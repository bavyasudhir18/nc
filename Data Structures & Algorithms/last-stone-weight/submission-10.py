class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            if a!=b:
                c=abs(a-b)
                heapq.heappush(stones, -c)
            
        if len(stones)>0:
            return -stones[0]
        return 0

        