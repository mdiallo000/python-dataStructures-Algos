from collections import defaultdict


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

        ownership = {}
        # {email : index of where withing the accounts lists it was found}
        disjointSet = UnionFind(len(accounts))
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in ownership:
                    _ = disjointSet.union(idx, ownership[email])
                ownership[email] = idx
        res = defaultdict(set)
        for i, account in enumerate(accounts):
            res[disjointSet.find(i)].update(account[1:])
        return [[accounts[i][0]] + sorted(list(email)) for i, email in res.items()]
