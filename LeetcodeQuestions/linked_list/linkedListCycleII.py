class Solution:
    def detectCycleNaive(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
