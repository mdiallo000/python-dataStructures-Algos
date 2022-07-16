class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        logs.sort(key=lambda i: i[0])

        popCount = 0

        res = [logs[0]]
        store_year = []
        for start, end in logs[1:]:

            prevEnd = res[-1][1]

            if start - 1 < prevEnd:
                popCount += 1
                store_year.append([prevEnd, popCount])
