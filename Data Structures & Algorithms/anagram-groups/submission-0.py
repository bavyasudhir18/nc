class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f=[]
        for i in strs:
            w={}
            for j in i:
                if j not in w:
                    w[j]=1
                else:
                    w[j]+=1
            if w not in f:
                f.append(w)
        a=[[] for _ in range(len(f))]
        for i in strs:
            k={}
            for j in i:
                if j not in k:
                    k[j]=1
                else:
                    k[j]+=1
            m=0
            for l in f:
                if l==k:
                    a[m].append(i)
                m+=1
        return a        