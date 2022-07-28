from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # since we want to go from  0 to => N-1, target node should be
        target = len(graph) - 1

        result = []

        def DFS(curr, path):

            # best case for when we should return
            if curr == target:
                result.append(path[:])
                return
            for node in graph[curr]:
                path.append(curr)
                DFS(node, path)
                path.pop()
            path = deque([0])

            DFS(0, path)
            return result
