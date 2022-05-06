from heapq import heapify
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = nums

        heapq.heapify(heap)

        largest = heapq.nlargest(k, heap)

        return largest[-1]
