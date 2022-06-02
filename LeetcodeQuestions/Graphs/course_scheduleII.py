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
        result = []
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
            visit.add(course)
            result.append(course)
            #  if everything goes well than we just need to return True
            return True

        # Now we run the algo for all of the course

        for course in range(numCourses):
            # if its imposible to take a course due to a cycle existing than we need to return an empty list
            if not top_sort(course):
                return []
        return result
