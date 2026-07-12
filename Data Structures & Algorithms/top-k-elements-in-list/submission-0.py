class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in nums:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        f=dict(sorted(f.items(), key=lambda item:item[1], reverse=True))
        f=list(f)

        return f[:k]
