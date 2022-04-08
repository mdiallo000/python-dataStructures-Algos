

from multiprocessing import dummy


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        while list1 and list2:
            if list1 < list2:
                dummy.next = list1
            elif list2 < list1:
                dummy.next = list2
            else:
                dummy.next = list1
                dummy.next = list2
        return dummy
