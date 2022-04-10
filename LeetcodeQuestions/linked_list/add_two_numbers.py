# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


from multiprocessing import dummy


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_link = ListNode()
        tail = dummy_link
        p, q = l1, l2
        carry = 0
        while p and q:
            x = p.val
            if p is None:
                x = 0
            y = q.val
            if q is None:
                q = 0
            sum_nodes = p + q+carry
            carry = sum_nodes // 2
            tail.next = LisNode(sum_nodes)

            tail = tail.next
            q = q.next
            p = p.next
        if carry > 0:
            tail.next = ListNode(carry)
        return dummy.next
