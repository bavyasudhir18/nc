class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        q=[]
        for i in range(len(arr)):
            max_ = -1
            for j in range(i+1, len(arr)):
                if arr[j]>max_:
                    max_ = arr[j]
            q.append(max_)

        return q
        