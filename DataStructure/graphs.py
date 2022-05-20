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
