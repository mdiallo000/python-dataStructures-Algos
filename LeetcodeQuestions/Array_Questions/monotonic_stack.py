class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #  so we are given an array of integers, only positive integers, no floating point values. We want to determine whether or not this list is either monotonically increasing or decreasing.
        #  What shoudl my approach be?
        #  NOT sure if there is a silver bullet for this problem. We have to our disposal a couple of patterns
        #  what if we do two checks one for increasing and another for deacreasing?
        def checKp
        #  In actuality all i need to check is if its not monotonic in its composition
        #  So rather than attempting to see whether or not its monotonic lets see if it isnt
        #  so how will i do it?
     #  maybe i can use a stack?
     #  Go through the list, if i find a number that is greater than the previous and future then we return false
        #  after we have at least two elements inside of the stack i can then check to see whether or not current is less than the element on top of the stack but greater than the element on stack[-2]. If it is then we return false
