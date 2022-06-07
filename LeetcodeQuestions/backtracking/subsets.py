

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #  Initially i did this question by using a whole lot of parameters but there is a simpler way of doing the prblem
        #  since we are interested in all the subsets of a particular list we need generate them recursively by adding elements in of part of the recursive tree and removing them in other parts
        result = []
        sub_sequence = []

        def sub(idx):
            #  our base case makes sure that we do not add more elements than we are allowed
            if idx >= len(nums):
                result.append(sub_sequence.copy())
                return
            #  we add the current elem in our nums array into this sequence
            sub_sequence.append(nums[idx])
            #  now we call our function again, and this task will be repeated for our subsquent indices
            sub(idx+1)
            #  we will now pop()
            sub_sequence.pop()
            #  Now call for the other side of the sequences
            sub(idx+1)
            #  for almost each initial call, a pair of calls will be made leading to a time complexity of 2^N
        sub(0)
        return result
