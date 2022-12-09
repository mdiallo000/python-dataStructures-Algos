class UnionFind:

    def __init__(self, n):
        self.parent = []
        self.rank = []
        for i in range(1, n + 1):
            #  at first every node will be a parent of itself
            self.parent[i] = i
            #  at first every node will have a rank of zero
            self.rank[i] = 0

    #  the union find data structures has a find and union method, the first helps find the ultimate parent of a node as while as apply path compression to improve the time complexity of future find operations. The union method unites the two nodes by first find the ultimae parents

    def find(self, node):
        current_parent = self.parent[node]

        while current_parent != self.parent[node]:
            self.parent[current_parent] = self.parent[self.parent[current_parent]]
            current_parent = self.parent[current_parent]
        return current_parent

    def union(self, n1, n2):
        #  we first find the ultimate parent of the nodes
        p1, p2 = self.find(n1), self.find(n2)
        #  if two nodes have the same parent then there is node need to unite them
        if p1 == p2:
            return False
        #  now we need to determine how we attach these two nodes based on their rank
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True
