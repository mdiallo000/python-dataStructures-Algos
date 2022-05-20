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


class Graph:
    def __int__(self):
        self.vertDictionary = {}
        self.numVertices = 0
