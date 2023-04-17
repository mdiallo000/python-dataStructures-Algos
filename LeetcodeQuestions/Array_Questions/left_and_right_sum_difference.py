class Solution:

    def sumDifference(nums):
        # so we need to return a LIST of a similar size as nums that has the answer where answer[i] =  leftsum[i] -  rightsum[i]

        #  ex [10,4,8,3]
        # ex [15,1,11,22]

        #       Input: nums = [10,4,8,3]
        # Output: [15,1,11,22]
        # Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
        # The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
        #  i am thinking of sum prefix type technique but can't really pin point it.
