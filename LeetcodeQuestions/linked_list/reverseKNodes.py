class Solution:
    def reverseKGroup(self, head, k):

    def reverseList(head, k):
        prev, curr = None, head
        while k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1
        return
