class Solution:
    def majorityElement(self, nums):
        dict = {}
        for n in nums:
            if n not in dict:
                dict[n] = 1
            
            else:
                dict[n] += 1
        
        output = max(dict, key=dict.get)
        
        return output