class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        n=n-1
        q=deque()
        q.append(n)
        while q:
            for i in range(len(q)):
                a=q.popleft()
                #print("a: ",a)
                p=[]
                if a==0:
                    return True
                for i in range(len(nums)):
                    if i!=a and i<a:
                        t=a-i
                        m=nums[i]-t
                        #print(n, i, t, m)
                        if m >= 0:
                            p.append(i)
            #print(p)
            q=deque(p)
        return False       