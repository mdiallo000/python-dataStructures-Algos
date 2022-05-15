from collections import defaultdict
from email.policy import default


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #  first we need to create the graph based on the edges we were given
        neighbors = defaultdict(list)
        seen = set()
    #   neighbors = {:[], :[]}
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        def dfs(graph, start, end):
            if start == end:
                return True
            if start in seen:
                return False

            for vertex in graph[start]:
                if dfs(graph, vertex, end):
                    return True

            return False

        return dfs(neighbors, source, destination)
