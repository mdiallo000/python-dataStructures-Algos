from collections import defaultdict
from email.policy import default


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for crs1, crs2 in prerequisites:
            graph[crs1].append(crs2)
