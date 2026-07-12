class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i]=cost[i]+min(cost[i+1], cost[i+2])
        return cost[0] if cost[0]<cost[1] else cost[1]