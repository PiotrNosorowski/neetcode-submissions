class Solution:
    def threeSum(self, nums):
        nums.sort()
        
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                result = nums[l] + nums[r]
                if result < -nums[i]:
                    l+=1
                elif result > -nums[i]:
                    r-=1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l+=1
        return output