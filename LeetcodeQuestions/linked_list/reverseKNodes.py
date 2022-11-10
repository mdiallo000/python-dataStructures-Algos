class Solution:
    def reverseKGroup(self, head, k):

        def reverseList(head, k):
            prev, curr = None, head

            while curr:
                nxt = curr.next
                curr.next = prev
