class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i in range(len(temperatures)):
            m=0
            for j in range(i+1,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    res.append(abs(i-j))
                    m=-1
                    break
            if m==0:
                res.append(m)
        return res        