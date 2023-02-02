class NodeList:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortList(head):
        curr = head
        data = []
        while curr:
            data.append(curr.val)
            curr = curr.next
        data.sort()

        curr = head
