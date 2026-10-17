class Solution:
    def productExceptSelf(self, nums):
        prefs = []
        suffs = []
        output = []
        
        n=1                          # as we multiply, cant be 0
        prefs.append(n)
        for i in range(len(nums) - 1):
            n *= nums[i]
            prefs.append(n)

        n=1
        suffs.append(n)
        for i in range(len(nums) - 1, 0, -1):
            n *= nums[i]
            suffs.append(n)
        
        suffs.reverse()

        for i in range(len(nums)):
            output.append(prefs[i] * suffs[i])

        return output

nums = [1,2,4,6]

sol = Solution()
sol.productExceptSelf(nums)
        