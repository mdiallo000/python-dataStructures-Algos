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
    #  time complexity is nlogn

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.K:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

#  we could've gone with an array and a sorted array but both would yield less efficient time complexities.
