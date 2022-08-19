class Solution:

    def reduceArray(self, nums):

        heap = nums
        heapq.heapify(heap)

        total = 0
