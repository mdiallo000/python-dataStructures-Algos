from itertools import starmap

from pkg_resources import cleanup_resources


class Solution:
    def climbStairs(self, n: int) -> int:

        # Appenrantly its all fibnocci
        def climb(stairs):
            if stairs == 1:
                return 1
            if stairs == 2:
                return stairs

            return climb(stairs - 1) + climb(stairs - 2)
        climb(n)
