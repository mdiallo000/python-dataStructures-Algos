class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #  first base case
        if not head:
            return None

        if not head.next:
            return head
        #  Now lets identify our current tail which will become the old tail since the Node at n -k will become the tail
        #  We also keep a count of the amount of nodes in our linked list in order to know where the new tail will be
        num_nodes = 0
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
        #  when we find the old tail now lets connect it to the head of the linked list
        old_tail.next = head

        #  now its time to find the new tail:
        new_tail = head

        while ()
