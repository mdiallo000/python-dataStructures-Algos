class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #  first base case
        if not head:
            return None

        if not head.next:
            return head
        #  Now lets identify our current tail which will become the old tail since the Node at n -k will become the tail
        old_tail = head
