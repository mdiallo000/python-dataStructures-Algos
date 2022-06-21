class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        difference = []
        for c1, c2 in costs:
            difference.append([c2-c1, c1, c2])
        difference.sort()
        total = 0

        for i in range(len(difference)):

            if i < len(difference) // 2:
                total += difference[i][2]
            else:
                total += difference[i][1]
        return total
