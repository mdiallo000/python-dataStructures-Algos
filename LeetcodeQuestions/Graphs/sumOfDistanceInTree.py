class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
        # initial the result for the distance of from each point is unknown so we will store zero in our result
        res = [0]*n
        # every node will start off with a score of one and as we find out how many nodes are below it we will then add that to the initial score
        score = [1] * n

        def dfs_count(curr, parent, depth):

            for child in graph[curr]:
                if child != parent:
