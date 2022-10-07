import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        res = ""
        wrd = [(-a, "a"), (-b, "b"), (-c, 'c')]

        for count, char in wrd:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
