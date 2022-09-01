
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

        first, second = head, prev
        while second:
            # since the second half might be shorter than the first if the list has odd number of nodes
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
