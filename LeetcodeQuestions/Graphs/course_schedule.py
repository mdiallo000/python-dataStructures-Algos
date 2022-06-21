from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

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
            if graph[course] == []:
                return True
            visited.add(course)

            for prereq in graph[course]:
                if not DFS(prereq):
                    return False
            visited.remove(course)
            graph[course] = []
            return True

        for course in graph:
            if not DFS(course):
                return False
        return True
