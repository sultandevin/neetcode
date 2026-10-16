class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        n = len(s)
        left = 0
        right = n - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
            
