class Solution:
    def detectCycleNaive(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def findIntersect():
            fast, slow = head

            while fast and fast.next:

                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return slow
            return None

        if not head:
            return None

        intersect = findIntersect()

        p1 = head
        p2 = intersect

        while res !=
