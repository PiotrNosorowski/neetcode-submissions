class Solution:
    def twoSum(self, nums, target):
        array = []
        
        for num in nums:
            result = target - num
            if result in array:
                return [array.index(result), len(array)]
            array.append(num)


nums = [3,4,5,6]
target = 7

sol = Solution()
sol.twoSum(nums, target)