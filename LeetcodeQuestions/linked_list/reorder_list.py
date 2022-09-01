
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # phase one find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
