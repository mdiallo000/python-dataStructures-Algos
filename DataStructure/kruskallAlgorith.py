#  Kruskal Algorithm will allow to create a minimum spanning Tree using a disjoint set

class UnionFind:

    def __init__(self, n):
        self.parent = {}
        self.rank = {}
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


def kruskal(edges, n):

    #  we need a heap to keep track of the minimum weights between edges, since we want to create the minimum spanning tree based on this information

    heap = []
    for n1, n2, w in edges:
        heapq.heappush(heap, [w, n1, n2])
    #  now we have created the heap we can go on using our disjoint set to create the spanning tree
    disjoint_set = UnionFind(n)
    #  our disjoint set will now create its parent object as well as its ranks
    min_spanning_tree = []

    while len(min_spanning_tree) < n-1:
        w, n1, n2 = heapq.heappop(heap)

        # we destructure the item from the top of the heap, and now we can try to union them together, if we aren't able to that means there already part of the same component and we need to avoid adding them into a min spanning tree to avoid cycles.

        if not disjoint_set.union(n1, n2):
            continue
        min_spanning_tree.append([n1, n2])
    return min_spanning_tree
