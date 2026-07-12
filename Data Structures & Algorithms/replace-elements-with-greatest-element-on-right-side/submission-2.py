class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        q=[0]*len(arr)
        rm=-1
        for i in range(len(arr)-1, -1, -1):
            q[i]=rm
            rm=max(rm, arr[i])
        return q
        