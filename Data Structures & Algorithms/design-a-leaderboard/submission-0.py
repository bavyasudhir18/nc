class Leaderboard:

    def __init__(self):
        self.playerId_Array=[]
        self.score_Array=[]
        self.n=0

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.playerId_Array:
            self.playerId_Array.append(playerId)
            self.score_Array.append(score)
            self.n+=1
        else:
            for i in range(len(self.playerId_Array)):
                if playerId == self.playerId_Array[i]:
                    self.score_Array[i]+=score
                    break
            
    def top(self, K: int) -> int:
        p=sorted(self.score_Array)
        p=p[::-1]
        return sum(p[0:K])

    def reset(self, playerId: int) -> None:
        if playerId in self.playerId_Array:
            for i in range(len(self.playerId_Array)):
                if playerId == self.playerId_Array[i]:
                    self.score_Array[i]=0
                    break
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)