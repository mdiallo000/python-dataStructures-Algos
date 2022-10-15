class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        t = 0
        for n in nums:
            t += n
            self.prefix.append(t)

    def sumRange(self, left: int, right: int) -> int:
