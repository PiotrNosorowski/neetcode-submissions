class Solution:
    def twoSum(self, nums, target):
        array = {}

        for idx, num in enumerate(nums):
            result = target - num
            if result in array:
                return [array[result], idx]
            array[num] = idx
        
nums = [4,5,6]
target = 10

sol = Solution()
sol.twoSum(nums, target)