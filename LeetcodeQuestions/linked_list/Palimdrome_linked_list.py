# Given the head of a singly linked list, return true if it is a palindrome.
# Input: head = [1,2,2,1]
# Output: true


class Solution:
    def isPalindrome(self, head):

    def findMiddle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def reverseLinkedlist(self, head):

        # The first solution gets it done but it is has a bIG O(n) time complexity and a Space complexity O(n) since we are using extra memory for our Stack and its size may increase as our list Updates.

        #  Second method is very efficient its O(n) Time complexity and O(1) constant space due to our use of Pointers
