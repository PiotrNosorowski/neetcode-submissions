class Solution:
    def rob(self, nums):
        best = []

        for i in range(len(nums)):
            if i == 0:
                best.append(nums[i])
            
            elif i == 1:
                best.append(max(nums[i], nums[i-1]))
            
            else:
                best.append(max(nums[i] + best[i-2], best[i-1]))
        
        return best[-1]