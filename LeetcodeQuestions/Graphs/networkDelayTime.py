from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict()
        for u, v, w in times:
            graph[u].append((v, w))
