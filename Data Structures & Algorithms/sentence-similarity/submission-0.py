class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        pairs=set()
        for i, j in similarPairs:
            pairs.add((i, j))
            pairs.add((j, i))
        if len(sentence1)!=len(sentence2):
            return False
        t=0
        m=0
        for i in range(len(sentence1)):
            if sentence1[i]==sentence2[i]:
                m+=1
            elif ((sentence1[i], sentence2[i])) in pairs:
                t+=1
        print(m, t)
        if m+t == len(sentence1):
            return True
        return False       