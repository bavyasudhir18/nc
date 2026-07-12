class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        r=0
        length = 0

        for l in range(len(s)):
            while r<len(s) and s[r] not in window:
                window.add(s[r])
                r+=1
                length = max(length, r-l)
            else:
                window.remove(s[l])
                
            
        return length