class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        arr=[]
        for i in range(len(s)):
            arr.append(s[i])
        for i in range(len(shift)):
            m=shift[i][1] % len(arr)
            if shift[i][0]==0:
                arr=arr[m:]+arr[:m]
            else:
                arr=arr[-m:] + arr[:-m]
        return "".join(arr)        