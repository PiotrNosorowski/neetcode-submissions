class Solution:
    def rob(self, nums):
        a = 0
        b = 0

        for n in nums:
            a, b = b, max(n + a, b)
        
        return b
            