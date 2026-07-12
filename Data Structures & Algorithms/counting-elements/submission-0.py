class Solution:
    def countElements(self, arr: List[int]) -> int:
        f={}
        j=0
        for i in arr:
            if i not in f:
                f[i]=[]
            f[i].append(j)
            j+=1
        s=0
        for i in range(len(arr)):
            if arr[i]+1 in f:
                s+=1
        return s