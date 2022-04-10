

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        curr = head

        while index != n:
            curr = curr.next
            index += 1

        curr.next = curr.next.next
