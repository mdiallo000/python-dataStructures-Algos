from typing import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        count = Counter(nums)

        while count:
