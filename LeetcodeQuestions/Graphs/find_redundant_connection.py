from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adjcency_List = defaultdict(list)
        visited = set()
        res = []

        def DFS(start, end):

            if start in visited:
                return False

            if start == end:
                return True

            visited.add(start)

            for neig in adjcency_List[start]:
                if DFS(neig, end):
                    return True
            return False

        for n1, n2 in edges:
            if DFS(n1, n2):
                res = [n1, n2]

            adjcency_List[n1].append(n2)
            adjcency_List[n2].append(n1)
        # ex:
        return res[-1]
        # {
        #     1:[2,3]
        #     2:[1,3]
        #     3:[2]
        # }
