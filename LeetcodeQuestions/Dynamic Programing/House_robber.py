class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}

        return self.rob_from(0, nums)

    def rob_from(self, idx, houses)
