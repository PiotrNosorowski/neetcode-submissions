class Solution:
    def maxArea(self, heights):
        
        l = 0
        r = len(heights) - 1
        
        max_capac = 0

        while l < r:
                logic_height = min(heights[l], heights[r])
                capac = logic_height * (r - l)
                max_capac = max(capac, max_capac)

                if logic_height == heights[l]:
                    l += 1
                else:
                    r -= 1
            
        return max_capac