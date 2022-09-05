class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #  taking care of edge cases
        if not lists or len(list) == 0:
            return None
        # now while we have lists remaining
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                #  we increment by two since we want pairs
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(mergedLists(l1, l2))

    def mergeList(self, l1, l2)
