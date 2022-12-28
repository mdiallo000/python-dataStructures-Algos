class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i: [] for i in range(numCourses)}
        cycle = set()
        visit = set()
        output = []

        for u, v in prerequisites:
            graph[u].append(v)

        def topSort(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)

            for pre in graph[course]:
                if not topSort(pre):
                    return False
            visit.add(course)
            cycle.remove(course)
            output.append(course)
            return True
        for c in range(numCourses):
            if not topSort(c):
                return
