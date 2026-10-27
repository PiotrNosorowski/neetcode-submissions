class Solution:
    def getConcatenation(self, nums):
        arr = []
        for n in nums:
            arr.append(n)
        
        ans = nums + arr

        return ans
        