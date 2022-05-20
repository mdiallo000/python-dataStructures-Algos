class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        #  we set the distance between node to be inf
        self.distance = float('inf')
        #  All nodes are thus far unvisited
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connection(self):
        return self.adjacent.keys()

    def get_vertex_value(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def set_previous(self, prev):
        self.previous = prev

    def set_visted(self):
        self.Visted = True

    def __str__(self):
        return str(self.id) + 'adjacent:' + str([x.id for x in self.adjacent])


class Graph:
    def __int__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def add_vertex(self, value):
        self.numVertices += 1
        newVertex = Vertex(value)

        self.vertDictionary[value] = newVertex
        return newVertex

    def get_vertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.add_vertex(frm)
        if to not in self.vertDictionary:
            self.add_vertex(to)
        self.vertDictionary[to].add_neighbor(self.vertDictionary[frm], cost)
