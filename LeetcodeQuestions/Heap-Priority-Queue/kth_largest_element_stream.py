from heapq import heapify
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minHeap, self.K = nums, k
        #  we take our inital collection of data and and turn it into a heap, this process will take O(n) time depeding on the size of our initial data
        heapq.heapify(self.minHeap)
        #  now we make sure the heap only contains the amount of data that we are interested in which is K
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    #  When it comes to adding new elements into the heap we need to consider several things
    def add(self, val: int) -> int:
