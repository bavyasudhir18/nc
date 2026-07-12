class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=''
        for c in s:
            if c.isalnum():
                newstr+=c.lower()
        if newstr==newstr[::-1]:
            return True
        return False