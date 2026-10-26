class Solution:
    def maxProfit(self, prices):
        
        buy = prices[0]    # cannot be zero
        best = 0

        for p in prices:
            buy = min(buy, p) 
            best = max(best, p - buy)

        return best 

# we are only interested in lowest buy and highest profit