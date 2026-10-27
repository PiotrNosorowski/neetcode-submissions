class Solution:
    def climbStairs(self, n):
        if n<=2:
            return n
        
        else:
            a, b = 1, 2
            for _ in range(3, n + 1):
                a, b = b, b+a
            return b