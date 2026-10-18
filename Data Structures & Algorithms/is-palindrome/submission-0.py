class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char
        s = cleaned

        if (len(s) % 2 == 0):
            forw = []
            backw = []
            for char in range(0, len(s) // 2):
                forw.append(s[char])
            
            for char in range((len(s) // 2), len(s)):
                backw.append(s[char])
            
            backw.reverse()

            return forw==backw
        
        if (len(s) % 2 != 0):

            forw = []
            backw = []
            for char in range(0, len(s) // 2):
                forw.append(s[char])
            
            for char in range(len(s) // 2 + 1, len(s)):
                backw.append(s[char])
            
            backw.reverse()

            return forw==backw
                