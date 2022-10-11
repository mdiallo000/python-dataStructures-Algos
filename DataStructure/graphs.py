
from collections import defaultdict, deque
from pickle import FALSE
import queue


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        #  graph = {V: [], V2: []}

    def add_edge(self, S, D):

        self.graph[S].append(D)
    #  a general bfs template for counting the different paths from one node to a target


def breath_first_search(start, target, visit):
    visit = set()
    length = 0
    visit.add(start)
    queue = deque()
    queue.append(start)

    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node == target:
                return length
            for edge in graph[node]:
                if edge not in visit:
                    visit.add(edge)
                    queue.append(edge)
        length += 1
    return length


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# # g.add_edge("new york", "Boston")
# # g.add_edge("new york", "Philly")
# # g.add_edge("Philly", "D.C")
# # g.add_edge("Boston", "Newark")
# g.breath_first_search(2)
