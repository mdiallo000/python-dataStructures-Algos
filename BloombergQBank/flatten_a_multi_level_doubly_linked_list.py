
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        dummy = Node(0)
        curr = dummy
        stack = [head]

        while stack:

            temp = stack.pop()
