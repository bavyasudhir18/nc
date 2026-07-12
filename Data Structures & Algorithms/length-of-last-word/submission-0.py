class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t=s.split(" ")
        q=[]
        for i in t:
            if i!="":
                q.append(i)

        return len(q[len(q)-1])

        