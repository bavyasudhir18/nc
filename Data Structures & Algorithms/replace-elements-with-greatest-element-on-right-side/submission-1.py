class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        q=[0]*len(arr)
        for i in range(len(arr)):
            m=-1
            for j in range(i+1, len(arr)):
                m=max(m, arr[j])
            q[i]=m

        return q
        