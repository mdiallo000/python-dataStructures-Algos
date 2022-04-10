# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


from multiprocessing import dummy


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2:
            if l1 is None:
                x = 0
            else:
                x = l1.val
            if l2 is None:
                y = 0
            else:
                y = l2.val
            sum_nums = y + x + carry
            carry = sum_nums/10
            curr.next = LisNode(sum_nums % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next
