class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}


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
