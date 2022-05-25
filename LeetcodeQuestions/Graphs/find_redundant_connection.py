from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adjcency_List = defaultdict(list)
        visited = set()
        for n1, n2 in edges:
            adjcency_List[n1].append(n2)
            adjcency_List[n2].append(n1)
        # ex:

        # {
        #     1:[2,3]
        #     2:[1,2]
        #     3:[2]
        # }
        def DFS(graph, start):
