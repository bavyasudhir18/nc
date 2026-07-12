class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        s=0
        count=0
        
        for r in range(len(arr)):
            if r-l+1 > k:
                if s/k >= threshold:
                    count+=1
                s-=arr[l]
                l+=1
            s+=arr[r]
        if s/k >= threshold:
            count+=1
        return count