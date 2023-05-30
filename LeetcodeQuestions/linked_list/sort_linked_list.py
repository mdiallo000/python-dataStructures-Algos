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
        for n in data:
            curr.val = n
            curr = curr.next
        return head


class Answer:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #  we will essentially try to apply merge sort on the link list
