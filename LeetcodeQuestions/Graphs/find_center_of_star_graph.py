from collections import defaultdict


class Solution:
    #     There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

    # You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

    # Example 1:

    # Input: edges = [[1,2],[2,3],[4,2]]
    # Output: 2
    # Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
    # Example 2:

    # Input: edges = [[1,2],[5,1],[1,3],[1,4]]
    # Output: 1

    def findCenter(self, edges):
        #  the problem is actually pretty easy.
        #  The center will be the node with the most edges
        #  all we need to do is use a hashtable

        count = defaultdict(int)

        for u, v in edges:
            count[u] += 1
            count[v] += 1

        for node, edge in count.items():
