class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(newS) - 1
    
        while l < r:
            if newS[l] == newS[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True

