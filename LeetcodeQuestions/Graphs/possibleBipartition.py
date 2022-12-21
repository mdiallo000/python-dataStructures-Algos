class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        groups = {i: None for i in range(1, n + 1)}

        def dfs(node, state):
            if not groups[node]:
                groups[node] = state
            else:
                return groups[node]

            for neigbor in graph[node]:

                if not dfs(neigbor, 2 if state == 1 else 1):
                    return False
            return True
