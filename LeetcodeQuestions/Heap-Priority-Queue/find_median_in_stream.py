import heapq


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        #  in order to maintain the heaps in a way where the median can be easily found we need to change the conditions of both heaps depending on whether the max heap has two more elements then the min heap and vice-versa
        heapq.heappush(self.small, -1 * num)
        #  we need to make sure that every value in the small heap is <= to the values in large heap
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # now we need to make sure that the amount of values in the small heap are not greater than 2 compared to the large heap, in other words we need to make sure it is balance
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        #  now we do the same for the opposite case
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) // 2
        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
