from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # def search(graph, vertex, visited, parent):
        #     visited[vertex] = True
        #     for neighbor in graph[vertex]:
        #         if not visited[neighbor]:
        #             if search(graph, neighbor, visited, vertex):
        #                 return True
        #         elif parent != neighbor:
        #             return True
        #     return False

        # def has_cycle(graph):
        #     visited = {v: False for v in graph.keys()}

        #     for vertex in graph.keys():
        #         if not visited[vertex]:
        #             if search(graph, vertex, visited, None):
        #                 return True
        #     return False
        graph = defaultdict(list)

        for Class1, Class2 in prerequisites:
            graph[Class1].append(Class2)

        #
        # {
        #     0:[1,6]
        #     1:[2,3]
        #     2:[5]
        #     3:[]
        #     5:[]
        # }
        visited = set()

        def DFS(course):
            if course in visited:
                return False
