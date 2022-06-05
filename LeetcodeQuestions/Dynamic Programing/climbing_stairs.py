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

            return climb(1-stairs) + climb(2-stairs)
