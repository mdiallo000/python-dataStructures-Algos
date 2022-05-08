import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #  points = [[3,3],[5,-1],[-2,4]]

        pts = []

        for x, y in points:
            distance = ((x)**2) + ((y) ** 2)
            pts.append([distance, x, y])
        #  [[18,3,3],[26,5,-1],[20,-2,4]]
        heapq.heapify(pts)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])

        return res
