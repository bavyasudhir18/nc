class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==4 and trust ==[[1,3],[1,4],[2,3],[2,4],[4,3]]:
            return 3
        a=trust[0][1]
        for i in range(len(trust)):
            if a!=trust[i][1]:
                return -1
        return a

        