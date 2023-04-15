class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #  taking care of edge cases
        if not lists or len(lists) == 0:
            return None
        # now while we have lists remaining
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                #  we increment by two since we want pairs
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        if l1 or l2:
            tail.next = l1, l2
        return dummy.next

# Lessons learned
    #  Could've been solved by making multiple comparison with each node in the list, but that would lead to a complexity of N * k
    #  A better way of solving was to by pass all of these individual comparisons and use mergeSort technique, doing so will improve time complexity by N * log K
