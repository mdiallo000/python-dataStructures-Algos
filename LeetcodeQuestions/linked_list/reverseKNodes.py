class Solution:
    def reverseKGroup(self, head, k):

        def reverseList(head, k):
            prev, curr = None, head
            count = 0
            while curr and count < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count += 1
            return
