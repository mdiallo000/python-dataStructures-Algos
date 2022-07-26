class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #  first base case
        if not head:
            return None

        if not head.next:
            return head
        #  Now lets identify our current tail which will become the old tail since the Node at n -k will become the tail
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
        #  when we find the old tail now lets connect it to the head of the linked list
        old_tail.next = head
