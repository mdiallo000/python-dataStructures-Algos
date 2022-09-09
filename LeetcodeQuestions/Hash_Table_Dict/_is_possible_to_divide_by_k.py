from typing import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)

        while count:
            minNum = min(count.keys())

            for i in range(k):

                if (minNum + i) in count:
                    if count[minNum + i] == 1:
                        del count[minNum + i]
                    else:
                        count[minNum + i] -= 1

                else:
                    return False
        return True
