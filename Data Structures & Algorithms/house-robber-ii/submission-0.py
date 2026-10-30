class Solution:
    def rob(self, nums):
        best_1 = []
        best_2 = []

        if len(nums) == 1:
            return nums[0]

        houses_1 = nums[:-1]
        houses_2 = nums[1:]

        for i in range(len(houses_1)):
            if i == 0:
                best_1.append(houses_1[i])
            
            elif i == 1:
                best_1.append(max(houses_1[i], houses_1[i-1]))
            
            else:
                best_1.append(max(houses_1[i] + best_1[i-2], best_1[i-1]))
        
        
        for i in range(len(houses_2)):
            if i == 0:
                best_2.append(houses_2[i])
            
            elif i == 1:
                best_2.append(max(houses_2[i], houses_2[i-1]))
            
            else:
                best_2.append(max(houses_2[i] + best_2[i-2], best_2[i-1]))

        
        return max(best_1[-1], best_2[-1])
        
        