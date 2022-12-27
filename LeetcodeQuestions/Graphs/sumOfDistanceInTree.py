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
        self.count = 0

        def dfs_count(curr, parent, depth):
            level = 1
            for child in graph[curr]:
                if child != parent:
                    level += dfs_count(child, curr, depth+1)
                    self.count += depth + 1
            score[curr] = level

        dfs_count(0, -1, 0)

        # our scores table has been filled and we also have info on the actual sumDistance for node 0 stored in self.count. Now after another dfs run we can apply the formula self.count + n - score[curr] - score[curr]. This will be applied for every posititon in our res

        def dfs(curr, parent, count):
            res[curr] = count
            for child in graph[curr]:
                if child != parent:
                    dfs(child, curr, count + (n - score[child] - score[child]))

        dfs(0, -1, self.count)
        return res
