"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        Printer = {}

        def DFS(node):
            if node in Printer:
                return Printer[node]

            copy = Node(node.val)
            Printer[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(DFS(neighbor))

            return copy

        return DFS(node)
