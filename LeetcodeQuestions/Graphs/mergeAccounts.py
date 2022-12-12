class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, node):

        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1:])
                graph[account[1:]].add(email)
                email_to_name[email] = name
        print(graph)
