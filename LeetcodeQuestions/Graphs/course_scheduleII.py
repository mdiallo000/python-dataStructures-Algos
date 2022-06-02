from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        #  We need to build some sort of adjecency list
        for crs1, crs2 in prerequisites:
            graph[crs1].append(crs2)

        #  now we need both a visited set that will keep track of the courses that have been taken and a cycle set that will make sure no cycles exits within the graph
        visit = set()
        cycle = set()

        #  now we will create the DFS function that will determine if a course can be taken

        def top_sort(course):
            #  righ away we should check wheter this course appears in our cycle
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)

            for preq in graph[course]:
                if not top_sort(preq):
                    return False
            cycle.remove(course)
