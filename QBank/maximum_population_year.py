class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        logs.sort(key=lambda i: i[0])

        popCount = 0

        res = [logs[0]]

        for start, end in logs[1:]:

            prevEnd = res[-1][1]
