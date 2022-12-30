from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #   So i am given a graph and our job is to find all possible paths from 0 to n-1
        #  When we deal with graphs we are concerned with avoiding cycles
        #  the graph we are given is directed, so there may be a chance of us not reaching the destination.
        #  first thing which comes to mind is the algorithm required to interacte and traverse the graph, in this case we have both DFS and BFS available to us.
        #  If we have this graph =  [ [0,1], [0,2], [2,3]]  then all possible paths starting from zero goes like this [0,1,3] and [0,2,3].
        #  So i would begin at zero go to one of its edges and add that edge to our output, continue on adding until we have reached our target, if we never reach the target on this path then there is no use of adding to our output
        #  so we will need a list that we will need to updated whenever we encounter new nodes
        #  Now how will my dfs function?
        #  Since we are concerned with generating all possible paths, i think this problem may include a bit of bactracking. What i mean by this is we will construct our path until we reach the target, once we reach our target we will then add the path into our result. and then we pop out the elements as we return back to the parent. Now the list is empty of the paths already explored and we can examine new paths

        adjacency_list = defaultdict()
        for u, v in enumerate(graph):
            adjacency_list[u] = v
        output = []
        target = len(graph) - 1

        def dfs(node, path):
            if node == target:
                path.append(node)
                output.append(path[::])
                return
            path.append(node)
            for edge in adjacency_list[node]:
                dfs(edge, path)
                path.pop()
            return
        dfs(0, [])

        return output

    #  This above implementation i think would actually work if the graph we are given maded it possible to create and adjency list. But overall my idea to backtrack whenver we complete a path is totally correct.
    #  I realized we could construct a proper adjacency_list by enumerating over the graph.
