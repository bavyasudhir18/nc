class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f={}
        j=0
        for i in nums:
            if i not in f:
                f[i]=j
            # f[i].append(j)
            j+=1
        
        print(f)
               
        for i in range(len(nums)):
            req_num = target-nums[i]
            if req_num in f:
                if i!=f[req_num]:
                    return sorted([i, f[req_num]])      