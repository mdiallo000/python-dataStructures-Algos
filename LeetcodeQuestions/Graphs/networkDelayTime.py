from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = defaultdict(list)
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
            t = max(t, w1)
            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visited) == n else -1

        # time complexity is O(e * logv)
        #  we used dikjstra shortest path algorithm since we want to find the shortest amount of time a signal can reach all points in the graph
