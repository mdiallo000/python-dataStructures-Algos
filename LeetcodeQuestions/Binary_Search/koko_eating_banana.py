from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # our goal is to find the minum number of bananas that kooko can eat before the guard come back at H hours. so we will be return total time

        l, r = 1, max(piles)
        k = 0

        while l <= r:
            mid = (l+r)//2
            total_time = 0
            for pile in piles:
                total_time += (pile - 1 // 2) + 1

            if total_time <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k
