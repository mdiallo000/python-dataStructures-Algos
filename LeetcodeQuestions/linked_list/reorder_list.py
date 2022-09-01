
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # phase one: find second
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # phase two: reverse the second half
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # last phase: reorder list
