import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        heap = [intervals[0][1]]
        heapq.heapify(heap)
        res = 0

        for start, end in intervals[1:]:

            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)
