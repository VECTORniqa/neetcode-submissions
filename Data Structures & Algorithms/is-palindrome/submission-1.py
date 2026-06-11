class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        for i in s:
            if not i.isalnum():
                s = s.replace(i, "")
        l = 0
        r = len(s) - 1



        while l < r:
            if s[l] == s[r]:
                r -= 1
                l += 1
            
            else:
                return False
        
        return True
                
        