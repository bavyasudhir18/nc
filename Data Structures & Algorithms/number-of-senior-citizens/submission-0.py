class Solution:
    def countSeniors(self, details: List[str]) -> int:
        s=0
        for i in details:
            m=i[11:13]
            m=int(m)
            if m>60:
                s+=1
        return s       