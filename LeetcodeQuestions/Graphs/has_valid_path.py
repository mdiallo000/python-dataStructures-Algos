from collections import defaultdict
from email.policy import default


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #  first we need to create the graph based on the edges we were given
        neighbors = defaultdict(list)
    #  neighbors = {:[], :[]}
