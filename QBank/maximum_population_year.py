class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        Map = {}

        for start, end in logs:

            for year in range(start, end):

                Map[year] = Map.get(year, 0)+1

        return sorted([i for i in Map.keys() if Map[i] == max(Map.values())])[0]
