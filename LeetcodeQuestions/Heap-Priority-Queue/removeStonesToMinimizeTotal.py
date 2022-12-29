class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #  we are given a list of numbers that represent the number of stones at that position. 
        #  Our goal is to return the minimum possible number of stones remaning after applying k operations
        #  The operation to be applied is this:
                #  we take a stone from the pile and then perform this operation on it math.ceil(pileValue/ 2) 
        #  Since we want minimize the number of stones remaning that should tell us that we need to prioritize the largest stones in the piles and perform the operation on them. By doing so we can minimize the total.
        #  [4,7,5,9] and K = 3
        #  so in this case we would take the nine, divide it by 2 and take the ceiling => 5
        #  [4,7,5,5]
        #  Next we take 7 since its next greatest value 7 => 4
        #  [4,4,5,5] 
        #  one more time we take a 5 => 3
        #  [4,4,5,3] we have reduced the piles total to be 16
        #  The data structure that will allow us to do this efficiently is a max heap 
        #  This way we can always select the greatest value in the maxHeap and perform the operations on that value. Repeat this k times.
        #  Pseudo Code:
            #  make a max heap by turning all the piles values into negatives since python does not have an in built max heap
            # Now that you have the max heap, pop from it k times, perform the operations on the heap node value and push it back into the heap 
            #  after take the total of the max heap 

            maxHeap =  [-i for i in piles]
            
            
            
            
            
            
          