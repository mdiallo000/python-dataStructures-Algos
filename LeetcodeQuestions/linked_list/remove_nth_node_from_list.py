

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        left = dummy
        right = head
    #    This first loop will jump start our right pointer a head by a distance of n

    #  Before
    #  dummy => 1 => 2 => 3=> 4 => 5 => None
    #  l        R
        while n > 0 and right is not None:
            right = right.next
            n -= 1
    #  After
    #  dummy => 1 => 2 => 3=> 4 => 5 => None
    #  l                  R
    # After we give our right pointer some distance of nth time now we can start moving the left and right together
        while right:
            right = right.next
            left = left.next

    #  Result of this loop
    #  dummy => 1 => 2 => 3=> 4 => 5 => None
    #                     L              R
    # Now we have l right before the nth node we want to remove
