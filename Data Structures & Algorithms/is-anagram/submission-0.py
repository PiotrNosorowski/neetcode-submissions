class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
            

s = "racecar"
t = "carrace"

sol = Solution()

sol.isAnagram(s, t)
