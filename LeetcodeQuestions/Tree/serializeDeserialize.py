
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # res = []
        # q = deque()
        # q.append(root)
        # while q:
        #     size = len(q)
        #     for _ in range(size):
        #         node = q.popleft()
        #         res.append("node")
        # return ",".join(res)
        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
