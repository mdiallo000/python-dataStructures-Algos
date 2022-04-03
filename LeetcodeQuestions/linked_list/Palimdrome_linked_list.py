# Given the head of a singly linked list, return true if it is a palindrome.
# Input: head = [1,2,2,1]
# Output: true


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        copy = curr
        while curr:
            copy = curr
            curr = curr.next
        while curr is not copy:
            if curr.val != copy.val:
                return False
        return True
