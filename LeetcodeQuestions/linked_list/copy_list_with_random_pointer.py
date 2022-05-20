"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


from typing import List


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        Printer = {None: None}
        curr = head
        while curr:
            # make a new Node from the original
            new_copied_node = ListNode(curr.val)
            # Now we store this new copy as a value of the curr original node
            Printer[curr] = new_copied_node
            # We move the current Pointer up
            curr = curr.next
        curr = head
        while curr:
            # lets get the copied node out of the Hashmap and start making some of these connections
            copy = Printer[curr]
            #  Now lets get its dot next connection
            copy.next = Printer[curr.next]
            copy.random = Printer[curr.random]
            curr = curr.next

        return Printer[head]
