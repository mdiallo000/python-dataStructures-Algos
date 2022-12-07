class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        heap = [intervals[0][1]]
        heapq.heapify(heap)
