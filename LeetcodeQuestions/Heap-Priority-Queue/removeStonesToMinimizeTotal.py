class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #  we are given a list of numbers that represent the number of stones at that position. 
        #  Our goal is to return the minimum possible number of stones remaning after applying k operations
        #  The operation to be applied is this:
                #  we take a stone from the pile and then perform this operation on it math.ceil(pileValue/ 2) 
        #  Since we want minimize the number of stones remaingn that should tell us o  