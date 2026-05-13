class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
    
        cleaned = ""
        for char in s:
            if char.isalnum():  # Keep only letters and numbers
                cleaned += char
        s = cleaned

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
        