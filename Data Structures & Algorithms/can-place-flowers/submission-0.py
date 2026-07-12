class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0:
            return True
        
        for i in range(len(flowerbed)):

            if i+1 < len(flowerbed):
                if flowerbed[0]==0 and flowerbed[1]==0:
                    flowerbed[0]=1
                    n-=1
                if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
                    flowerbed[len(flowerbed)-1]=1
                    n-=1
            if i+2 < len(flowerbed):
                if flowerbed[i]==0 and flowerbed[i+2]==0:
                    if flowerbed[i+1]==0:
                        flowerbed[i+1]=1
                        n-=1
            #print(flowerbed, n)
        return True if n<=0 else False
        
        
        