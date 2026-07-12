class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a=[]
        f={}
        for i in range(len(points)):
            a.append((points[i][0]-0)**2 + (points[i][1]-0)**2)
            d=(points[i][0]-0)**2 + (points[i][1]-0)**2
            if d not in f:
                f[d]=[]
            f[(points[i][0]-0)**2 + (points[i][1]-0)**2].append(points[i])
        a=sorted(a)
        m=0
        b=[]
        for i in sorted(f.keys()):
            for j in f[i]:
                b.append(j)
                m+=1
                if k==m:
                    return b       