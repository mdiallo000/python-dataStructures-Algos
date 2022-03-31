# Given the head of a singly linked list, reverse it in-place.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class solution:
def reverseList(self, head: Optional[ListNode]):
    # 1=> 2=> 3=> 4=>5=> None
    # H
    # None<==1<== 2<== 3<==4<==5
    #                          H
    prev = None
    current = head
    while current:
        after_curr = current.next
        current.next = prev
        prev = current
        current = after_curr
    return prev
