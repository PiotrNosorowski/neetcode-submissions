class Solution:
    def longestConsecutive(self, nums):
        
        nums = set(nums)
        longest = 0

        for n in nums:
            value = n - 1
            if value not in nums:   # a potential series beginning
                length = 0
                while (n+length) in nums:
                    length = length + 1
                longest = max(length, longest)

        return longest


        