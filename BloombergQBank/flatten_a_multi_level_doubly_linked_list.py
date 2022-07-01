
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        dummy = Node(0)
        curr = dummy
        stack = [head]
        while stack:
            temp = stack.pop()
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            curr.next = temp
            temp.prev = curr
            temp.child = None
            curr = temp
        dummy.next.prev = None
        return dummy.next
