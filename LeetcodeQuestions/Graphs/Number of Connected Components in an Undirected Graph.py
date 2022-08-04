from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n, e in edges:
            graph[n].append(e)
            graph[e].append(n)
        seen = [False] * n

        def DFS(node):

            for edge in graph[node]:
                if edge not in seen:
                    seen[edge] = True
                    DFS(edge)
        count = 0
        for i in range(n):
            if i not in seen:
                seen[i] = True
                count += 1
                DFS(i)

        return count
