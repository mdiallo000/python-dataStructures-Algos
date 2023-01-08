class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost) < sum(gas):
            return -1

        total = 0
        res = 0
