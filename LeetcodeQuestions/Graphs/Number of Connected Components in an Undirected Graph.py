from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n, e in edges:
            graph[n].append(e)
            graph[e].append(n)
        seen = [False] * n

        def DFS(node):

            if edge in graph[node]:
                if edge not in seen:
