from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict()
        for u, v, w in times:
            graph[u].append((v, w))
        minHeap = [(0, k)]
        t = 0
        visited = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
