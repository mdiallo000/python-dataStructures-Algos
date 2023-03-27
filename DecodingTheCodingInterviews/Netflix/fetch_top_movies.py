class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    #     # We’ll be given n lists that are all sorted in ascending order of popularity rank. We have to combine these lists into a single list that will be sorted by rank in ascending order, meaning from best to worst.
    # Since our task involves multiple lists, you should divide the problem into multiple tasks, starting with the problem of combining two lists at a time. Then, you should combine the result of those first two lists with the third list, and so on, until the very last one is reached.

    # Let’s discuss how we will implement this process:

    # Consider the first list as the result, and store it in a variable.

    # Traverse the list of lists, starting from the second list, and combine it with the list we stored as a result. The result should get stored in the same variable.

    # When combining the two lists, like l1 and l2, maintain a prev pointer that points to a dummy node.

    # If the value for list l1 is less than or equal to the value for list l2, connect the previous node to l1 and increment l1. Otherwise, do the same but for list l2.

    # Keep repeating the above step until one list points to a null value.

    # Connect the non-null list to the merged one and return.

    # # Let’s look at the code for the solution below:
    #  this problem is essentially merge k list
    #  we perform a routine merge between two lists
    def mergeList(self, l1, l2):
        dummy = ListNode(-1)

        tail = dummy

        while l1 or l2:
            if l1.val < l2.val:
                tail.next, l1, =
        tail.next = l1 or l2
