class Solution:
    def longestPalindrome(self, s):
        output = ""

        for i in range(len(s)):
            l = i
            r = i
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r + 1 - l > len(output):
                    output = s[l:r+1]
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r + 1 - l > len(output):
                    output = s[l:r+1]
                l -= 1
                r += 1
        
        return output








# two cases must be considered:
# a middle with two signs and a middle with one sign
        
                    
        

            

