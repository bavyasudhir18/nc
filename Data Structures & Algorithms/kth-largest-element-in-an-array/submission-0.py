class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-i for i in nums]
        heapq.heapify(nums)
        for i in range(k):
            r=heapq.heappop(nums)
        return -1*r        