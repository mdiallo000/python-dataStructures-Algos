
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0

        while True:

            slow = nums[slow]
            fast = fast[nums[fast]]

            if slow == fast:
                break

        new_slow = 0

        while True:
