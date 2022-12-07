class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))
