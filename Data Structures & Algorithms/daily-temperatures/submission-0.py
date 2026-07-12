class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[]

        for i in range(len(temperatures)):
            q=0
            for j in range(i+1,len(temperatures)):
                q=q+1
                if temperatures[j]>temperatures[i]:
                    a.append(q)
                    break
                if j==len(temperatures)-1:
                    a.append(0)

        while len(a)<len(temperatures):
            a.append(0)

        return a 