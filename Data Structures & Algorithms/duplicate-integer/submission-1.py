class Solution:
    def hasDuplicate(self, nums):
        set_ = set()

        for num in nums:
            if num in set_:
                return True
            set_.add(num)
        
        return False

nums = [1, 2, 3, 4]

sol = Solution()
sol.hasDuplicate(nums) 


        