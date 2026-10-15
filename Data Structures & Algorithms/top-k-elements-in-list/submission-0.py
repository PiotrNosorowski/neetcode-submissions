class Solution:
    def topKFrequent(self, nums, k):
        dict = {}   
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        output = []
        for i in range(0, k):
            high_key = max(dict, key=dict.get)
            output.append(high_key)
            del dict[high_key]
        
        return output


nums = [1, 1, 1, 2, 3]
k = 1
sol = Solution()
sol.topKFrequent(nums, k)