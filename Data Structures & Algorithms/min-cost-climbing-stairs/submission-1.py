class Solution:
    def minCostClimbingStairs(self, cost):
        total_cheapest = []

        for i in range(len(cost) + 1):
            if i <= 1:
                total_cheapest.append(cost[i])
            
            elif i == len(cost):
                first_backw = total_cheapest[i-1]
                second_backw = total_cheapest[i-2]
                total_cheapest.append(min(first_backw, second_backw))

            else:
                first_backw = total_cheapest[i-1] + cost[i]
                second_backw = total_cheapest[i-2] + cost[i]
                total_cheapest.append(min(first_backw, second_backw))
            
        return total_cheapest[-1]

