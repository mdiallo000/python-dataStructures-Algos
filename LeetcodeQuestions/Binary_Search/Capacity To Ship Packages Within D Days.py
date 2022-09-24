class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # A conveyor belt has packages that must be shipped from one port to another within days days.

        # The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

        # Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

        l, r = max(weights), sum(weights)

        while l < r:

            mid = l + r // 2

            if self.isValid(mid, weights, days):
                r = mid
            else:
                l = mid + 1
        return r

    def isValid(self, candidate, weights, days):
