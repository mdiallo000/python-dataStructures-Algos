class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #  Another DP question
        #  we will first append 0 to our list to make the computation possible
        #  test case [10,15,20]
        cost.append(0)
        #  test case [10,15,20, 0]

        for i in range(len(cost)-3, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        return min(cost[0], cost[1])
