import heapq
from os import scandir


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #  very simple solution if you understand the intuition
        #  we nee to put all the stones in a max heap to help us get the largerts weighing stones on top
        #  USE LISt comprehension to convert all the values to negatives
        # before = [2,7,4,1,8,1]

        stones = [-s for s in stones]

        #after = [-2,-7,-4,-1,-8,-1]
        heapq.heapify(stones)

        while len(stones) > 1:

            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first > second:
                val = -abs(first - second)
                heapq.heappush(stones, val)
        return abs(stones[0])
