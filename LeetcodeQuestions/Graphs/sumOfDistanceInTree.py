class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
        # initial the result for the distance of from each point is unknown so we will store zero in our resulr
        res = [0]*n
