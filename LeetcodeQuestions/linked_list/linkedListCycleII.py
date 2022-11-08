class Solution:
    def detectCycleNaive(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
