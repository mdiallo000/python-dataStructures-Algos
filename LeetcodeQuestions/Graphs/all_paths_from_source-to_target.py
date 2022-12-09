class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1

        result = []

        def DFS(curr, path):

            # best case for when we should return
            if curr == target:
                result.append(list(path))
                return
            for node in graph[curr]:
                path.append(node)
                DFS(node, path)
                path.pop()
        path = deque([0])

        DFS(0, path)
        return result
