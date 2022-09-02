class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        #  in order to maintain the heaps in a way where the median can be easily found we need to change the conditions of both heaps depending on whether the max heap has two more elements then the min heap and vice-versa
        heapq.heappush(self.small, -1 * num)

    def findMedian(self) -> float:
        if self.heap
        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
