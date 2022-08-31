class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        #  [3,6,1,2,5,7], k = 2
        #  [1,2,3]  [6,5]

        heap = nums

        heapq.heapify(heap)
        res = []
        while heap:
            subs = []
            first = heapq.heappop(heap)
            if heap[0] - first <= k:
                subs.append(first)
