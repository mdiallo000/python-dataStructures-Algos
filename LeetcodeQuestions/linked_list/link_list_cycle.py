# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow, fast = head, head
        #     s       f
        # 1=> 2=> 3=>4=>
        #      ^
        #      <== <== <==
        while fast and fast.next.next:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                return True
        return False
