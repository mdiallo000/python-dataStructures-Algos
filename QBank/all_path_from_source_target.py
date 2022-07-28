class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # since we want to go from  0 to => N-1, target node should be
        target = len(graph) - 1

        result = []

        def DFS(curr, target)

        # best case for when we should return
