class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            b=s[0:i] + s[i+1:len(s)]
            if b==b[::-1]:
                return True
        return False