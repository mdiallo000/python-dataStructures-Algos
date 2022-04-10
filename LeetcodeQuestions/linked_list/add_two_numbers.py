# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


from multiprocessing import dummy


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_link = ListNode()
        tail = dummy_link

        while l1 and l2:
            tail.next = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
        return dummy_link.next
