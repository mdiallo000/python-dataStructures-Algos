from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #  first we need to create the graph based on the edges we were given
        neighbors = defaultdict(list)
        seen = set()
    #   neighbors = {:[], :[]}
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        def dfs(start, end, seen):
            if start == end:
                return True
            if start in seen:
                return False
            seen.add(start)

            for vertex in neighbors[start]:
                if dfs(vertex, end, seen):
                    return True

            return False

        return dfs(source, destination, seen)
