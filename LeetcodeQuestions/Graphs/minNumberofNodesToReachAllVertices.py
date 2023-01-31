class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = {}

        for i in range(n):
            graph[i] = 0

        for src, target in edges:
            graph[target] += 1
        res = []

        for node in graph:

            if graph[node] == 0:
                res.append(node)
        return res
