class Solution:
    def detectCycleNaive(self, head):

        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next
        return None

    def detectCycle(self, head):

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
        if not intersect:
            return None
        p1 = head
        p2 = intersect

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
