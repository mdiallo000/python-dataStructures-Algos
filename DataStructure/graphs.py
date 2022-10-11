
from collections import defaultdict, deque
from pickle import FALSE
import queue


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        #  graph = {V: [], V2: []}

    def add_edge(self, S, D):

        self.graph[S].append(D)

    def breath_first_search(self, start, target, visit):
        visit = set()
        length = 0
        visit.add(start)
        queue = deque()
        queue.append(start)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# g.add_edge("new york", "Boston")
# g.add_edge("new york", "Philly")
# g.add_edge("Philly", "D.C")
# g.add_edge("Boston", "Newark")
g.breath_first_search(2)
