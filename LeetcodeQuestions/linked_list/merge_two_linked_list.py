

from multiprocessing import dummy


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        while list1.val and list2.val:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2

        return dummy
