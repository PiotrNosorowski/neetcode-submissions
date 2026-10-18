class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char
        s = cleaned

        return s == s[::-1]
        