class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #  i guess this is a stack question since we will get the scores first and then the operations that must be applied on these scores. With the stack we can pop off the elements which came before and apply the logic that needs to be applied.
        #  so we will create the stack using the array, next we will then apply the opertions on the stack depending on whatever is required
        #  ex [5,2,c,d,+]
        #   [5] => 2[5,2] => c[ 5] => d[ 10] => +[5] => answer should 5
        #  5 => [5] => -2 [5,-2] =>4 [5,-2,4] => c [5, -2 ] => d [5 ,-4] => 9 [5,-4,9] => + [5,-4, 9, 5, 14] => + [18] => answer should be 18
