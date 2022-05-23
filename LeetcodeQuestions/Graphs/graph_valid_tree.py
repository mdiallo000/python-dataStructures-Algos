from collections import defaultdict
from email.policy import default


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not n:
            return True
        graph = defaultdict(list)
        visited = set()
        # n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        #  we construct a graph
        # {
        #     0:[1,2,3]
        #     1:[0,4]
        #     2:[0]
        #     3:[0]
        #     4:[1]
        # }

        def DFS(start, prev):
            if start in visited:
                return False
            visited.add(start)
            for n in graph[start]:

                if n == prev:
                    continue
                if not DFS(n, start):
                    return False
            return True

        return DFS(0, -1) and len(visited) == n
